import unittest
from pathlib import Path

import click
from click.testing import CliRunner

from task2 import grep_input, grep_file

class Test_task0(unittest.TestCase):
    def test_file(self):

        runner = CliRunner()
        result = runner.invoke(grep_file, ['if', 'task0.py', 'task3.py'])
        self.assertTrue('3 occurrences in 80 rows.' in result.output)

    def test_input(self):
        runner = CliRunner()
        result = runner.invoke(grep_input, ['int'], input=
                               '''int: line_count - count of occurrence.int: total_count - total processed rows''')
        self.assertTrue('2 occurrences in 1 rows' in result.output)

if __name__ == '__main__':
    unittest.main()
