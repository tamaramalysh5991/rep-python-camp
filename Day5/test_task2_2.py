import unittest
import os
from task2_click import grep_files, grep_stdin
from click.testing import CliRunner


class TestTask2(unittest.TestCase):

    def setUp(self):
        self.grep_files = grep_files

    def test_input(self):
        """Test to check __main__"""
        result = os.system("python task2_click.py def task1.py")
        self.assertEqual(result, 0)

    def test_exp(self):
        """Test to check the output of the exception"""
        runner = CliRunner(echo_stdin=True)
        result = runner.invoke(grep_files, ['def', 'task.py', 'task.py'])
        self.assertTrue(result.exit_code == 2)
        self.assertTrue('Error' in result.output)

    def test_files(self):
        """Test to check files input"""
        runner = CliRunner()
        result = runner.invoke(grep_files, ['def', 'task1.py', 'task3.py'])
        self.assertTrue(result.exit_code == 0)
        self.assertTrue('def' in result.output)
        self.assertTrue('Total: 3 occurrences in 54 rows.' in result.output)

    def test_stdin(self):
        """Test to check standart input"""
        runner = CliRunner()
        result = runner.invoke(grep_stdin, ['def'], input=
                               '''def testdef_ testdef def exp(self)\n Tota def l: 3def occdefurr def ences in 54 rows.,\n''')
        self.assertTrue(result.exit_code == 0)
        self.assertTrue('8 occurrences in 2 rows' in result.output)
        self.assertTrue('def' in result.output)


if __name__ == '__main__':
    unittest.main()