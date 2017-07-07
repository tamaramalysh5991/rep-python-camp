#!/usr/bin/env python
""" Create GREP-like CLI tool using python’s generators that takes PATTERN as
    param and match incoming data from stdin or from unlimited set of
    files passaed as params as well. Unix pipes should be supported as well.

    Examples of use case that should work:
            ./grep.py PATTERN < test.py (stdin)
            ./grep.py PATTERN file1 file2 etc
            cat file1 | ./grep.py PATTERN
            find . -iname '*.py' | ./grep.py PATTERN
            ./grep.py -h -> should print small help

            the CLI tool should output matched text
            the CLI tool should output matched stats like Matched 3 out of 5000
            the CLI tool should output help
            the PATTERN param is just a text (not a regexp)

    for implementing CLI functionality you can use ANY pip packages.
"""
from argparse import ArgumentParser, FileType
from sys import stdin


def input_file(pattern, files):
    """Function return search results from files input.
    Args:
        pattern(string) - Word used for search.
        files (file)- List of received files.
    Return:
        list: rows with an occurrence pattern.
    Yields:
        int: line_count - count of occurrence.
        int: total_count - total processed rows
    """
    line_count = 0
    total_count = 0
    line_all = []
    for f in files:
        for line in open(f):
            if pattern in line:
                line_count += 1
                line_all.append(line)
            total_count += 1
    line_all = ('\n'.join(line_all))
    yield (line_count, total_count, line_all)


def standard_input(pattern, lines):
    """Funcrion return search results from standard input.
    Args:
        pattern(string) - Word used for search.
        lines(list)- Rows.
    Return:
        list: rows with an occurrence pattern.
    Yields:
        int: line_count - count of occurrence.
        int: total_count - total processed rows
    """
    lines = iter(lines)
    line_count = 0
    total_count = 0
    line_all = []
    for line in lines:
        if pattern in line:
            line_all.append(line)
            line_count += 1
        total_count += 1
    line_all = ('\n'.join(line_all))
    yield (line_count, total_count, line_all)


def grep():

    parser = ArgumentParser(prog='grep.py',
                            usage='''
                            %(prog)s PATTERN file1 file2 or < test.py (stdin)
                            cat file1 | %(prog)s PATTERN
                            find . -iname '*.py' | %(prog)s PATTERN''')

    parser.add_argument('pattern', help='Pattern is searched in files')
    return_print = 'Total: %d event in %d rows.\n\n%s'

    if not stdin.isatty():
        """Detect if someone is piping data into program,
        or running it interactively
        """
        args = parser.parse_args()
        total, find, lines = next(standard_input(args.pattern, stdin))
        return return_print % (total, find, lines)
    else:
        """Return count of pattern in lines from files."""
        parser.add_argument('files', nargs='+',
                            help='Files to be searched', type=FileType())
        args = parser.parse_args()
        total, find, lines = next(input_file(args.pattern, args.files))
        return return_print % (total, find, lines)


if __name__ == '__main__':
    print(grep())
