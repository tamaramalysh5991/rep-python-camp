#!/usr/bin/env python
from sys import stdin

import click


def search_in_files(pattern, files):
    """Funcrion return search results from files input.
    Args:
        pattern(string) - Word used for search.
        files (file)- List of received files.
    Yields:
        int: line_count - count of occurrence.
        int: all_processed - total processed rows
        list: find_rows - rows with pattern
    """
    encounters = 0
    all_processed = 0
    find_rows = []
    for f in files:
        for line in f:
            if pattern in line:
                encounters += 1
                find_rows.append(line)
            all_processed += 1
    find_rows = ('\n'.join(find_rows))
    yield (encounters, all_processed, find_rows)


def search_lines(pattern, lines):
    """Funcrion return search results from files input.
    Args:
        pattern(string) - Word used for search.
        lines (iter)- List of received lines.
    Yields:
        int: line_count - count of occurrence.
        int: all_processed - total processed rows
        list: find_rows - rows with pattern"""
    lines = iter(lines)
    encounters = 0
    all_processed = 0
    find_rows = []
    for line in lines:
        if pattern in line:
            for in_line in line.split():
                if pattern in in_line:
                    encounters += 1
            find_rows.append(line)
        all_processed += 1
    find_rows = ('\n'.join(find_rows))
    yield (encounters, all_processed, find_rows)


CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
def cli():
    ''' task_2.py is programm for find occurrence PATTERN in files\n
        ./task_2.py  PATTERN file1 file2 or < test.py (stdin)\n
        \b
        cat file1 | ./task_2.py PATTERN\n
        find . -iname '*.py' | ./task_2.py  PATTERN
    '''
    pass


@click.command()
@click.argument('pattern', type=str)
@click.argument('files', nargs=-1, type=click.File('r'))
def grep_file(pattern, files):
    """Search in file (./task2_click.py  PATTERN file1 file2)"""
    result = 'Find lines: \n%s\n %d occurrences in %d rows.\n'
    encounters, all_processed, find_rows = next((search_in_files(pattern, files)))
    click.secho(result % (find_rows, encounters, all_processed), fg='blue')


@click.command()
@click.argument('pattern', nargs=1, type=str)
def grep_input(pattern):
    """Search in lines (/task_2.py  PATTERN < test.py (stdin)"""
    result = 'Find lines: \n%s\n %d occurrences in %d rows.\n'
    input_stream = click.get_text_stream('stdin')
    encounters, all_processed, find_rows = next(search_lines(pattern, input_stream))
    click.secho(result % (find_rows, encounters, all_processed), fg='blue')


if __name__ == '__main__':  # pragma: no cover
    if not stdin.isatty():
        grep_input()
    else:
        grep_file()
