import filecmp
import re
import unittest

from DependenciesValidator import DependenciesValidator
from Exceptions import FileNodeException, DependenciesValidatorException
from FileNode import FileNode
from FileWriter import FileWriter

REGEX_REPLACE_PATTERN = "{{%([^(\r\n|\r|\n)]*)%}}"


class FileNodeTests(unittest.TestCase):
    def setUp(self):
        self.__regex_matcher = re.compile(REGEX_REPLACE_PATTERN)

    def test_valid(self):
        file_node = FileNode("valid.md", self.__regex_matcher)
        self.assertEqual(file_node.file_path, "valid.md")
        self.assertEqual(file_node.dependencies, [])
        file_node = FileNode("./valid_test_file.md", self.__regex_matcher)
        self.assertEqual(file_node.file_path, "./valid_test_file.md")
        self.assertEqual(file_node.dependencies, ["valid.md"])

    def test_doesnt_exist(self):
        with self.assertRaises(FileNodeException):
            file_node = FileNode("i_dont_exist.md", self.__regex_matcher)


class DependenciesValidatorTests(unittest.TestCase):
    def setUp(self):
        self.__regex_matcher = re.compile(REGEX_REPLACE_PATTERN)

    def test_valid(self):
        validator = DependenciesValidator("./valid_test_file.md", self.__regex_matcher)
        validator.validate()

    def test_valid_but_not_tree(self):
        validator = DependenciesValidator("./valid_but_not_tree.md", self.__regex_matcher)
        validator.validate()

    def test_invalid(self):
        validator = DependenciesValidator("./invalid.md", self.__regex_matcher)
        with self.assertRaises(DependenciesValidatorException):
            validator.validate()
        validator = DependenciesValidator("./invalid_father.md", self.__regex_matcher)
        with self.assertRaises(DependenciesValidatorException):
            validator.validate()

    def test_circular(self):
        validator = DependenciesValidator("./first_order_circular.md", self.__regex_matcher)
        with self.assertRaises(DependenciesValidatorException):
            validator.validate()
        validator = DependenciesValidator("./half_circular_1.md", self.__regex_matcher)
        with self.assertRaises(DependenciesValidatorException):
            validator.validate()
        validator = DependenciesValidator("half_circular_2.md", self.__regex_matcher)
        with self.assertRaises(DependenciesValidatorException):
            validator.validate()


class FileWriterTests(unittest.TestCase):
    def setUp(self):
        self.__regex_matcher = re.compile(REGEX_REPLACE_PATTERN)

    def test_valid(self):
        with open("valid.md", "r") as f:
            with open("valid_output.md", "w") as g:
                file_writer = FileWriter(f, g, self.__regex_matcher)
                file_writer.write()
        self.assertEqual(filecmp.cmp('valid_output.md', 'valid_expected.md'), True)

    def test_valid_test_file(self):
        with open("valid_test_file.md", "r") as f:
            with open("valid_test_file_output.md", "w") as g:
                file_writer = FileWriter(f, g, self.__regex_matcher)
                file_writer.write()
        self.assertEqual(filecmp.cmp('valid_test_file_output.md', 'valid_test_file_expected.md'), True)

    def test_valid_but_not_tree(self):
        with open("valid_but_not_tree.md", "r") as f:
            with open("valid_but_not_tree_output.md", "w") as g:
                file_writer = FileWriter(f, g, self.__regex_matcher)
                file_writer.write()
        self.assertEqual(filecmp.cmp('valid_but_not_tree_output.md', 'valid_but_not_tree_expected.md'), True)


if __name__ == '__main__':
    unittest.main()
