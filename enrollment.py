"""
Read data from CSV files, either to process line by line or to keep in some data structure.

Associate codes from the "Major" column in roster_selected.csv with corresponding codes from the "Code" column in programs.csv to find program names corresponding to each major code.

For example, if we see SO,ESCI in roster file, we will want to find the code "ESCI" from a record in the programs file to find that "ESCI" stands for "Environmental Science".

Count the number of rows containing each major.

Sort the data so that we can print the majors with the largest counts first.
"""

"""Enrollment analysis:  Summary report of majors enrolled in a class.
CS 210 project, Fall 2023.
Author:  Charlie Cooper
Credits: TBD
"""
import doctest
import csv

ROSTER = "test_roster.csv"

def read_csv_column(path: str, field: str) -> list[str]:
    """Read one column from a CSV file with headers into a list of strings.

    >>> read_csv_column("data/test_roster.csv", "Major")
    ['DSCI', 'CIS', 'BADM', 'BIC', 'CIS', 'GSS']
    
    """

    res = []

    with open(path,'r', newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            res.append(row[field])
    return res

def counts(column: list[str]) -> dict[str, int]:
    """Returns a dict with counts of elements in column.

    >>> counts(["dog", "cat", "cat", "rabbit", "dog"])
    {'dog': 2, 'cat': 2, 'rabbit': 1}
    """
    el_counts = {}
    for item in column:
        if item not in el_counts:
            el_counts[item] = 1
        else:
            el_counts[item]+=1
    return el_counts

def read_csv_dict(path: str, key_field: str, value_field: str) -> dict[str, dict]:
    """Read a CSV with column headers into a dict with selected
    key and value fields.

    >>> read_csv_dict("data/test_programs.csv", key_field="Code", value_field="Program Name")
    {'ABAO': 'Applied Behavior Analysis', 'ACTG': 'Accounting', 'ADBR': 'Advertising and Brand Responsibility'}
    """

    res = {}

    with open(path,'r', newline = '') as f:
        reader = csv.DictReader(f)
        for row in reader:
            res[row[key_field]] = row[value_field]
    return res

def items_v_k(majorCounts: dict):
    res =[]
    for code, count in majorCounts.items():
        pair = (count, code)
        res.append(pair)
    return res

def main():
    print(doctest.testmod())
    majors = read_csv_column("data/roster_selected.csv", "Major")
    counts_by_major = counts(majors)
    program_names = read_csv_dict("data/programs.csv", "Code", "Program Name")
    by_count = items_v_k(counts_by_major)
    by_count.sort(reverse=True)  # From largest to smallest
    for count, code in by_count:
        program = program_names[code]
        print(count, program)
    

if __name__ == "__main__":
    main()