import argparse
import re

from DependenciesValidator import DependenciesValidator
import settings
from Exceptions import AppException
from FileWriter import FileWriter


class EmbedMarkdownTool:
    """ This is the main class of the whole project

    """
    def __init__(self):
        """ Constructor for the class

        """

        parser = argparse.ArgumentParser(description="Build a final markdown file with embedded files "
                                                             "using the pattern from settings.py")
        parser.add_argument('main_file_path', type=str, help="the path to the main markdown file")
        parser.add_argument('destination_file_path', type=str, help="the path to the destination file")
        self.__args = parser.parse_args()
        self.__regex_matcher = re.compile(settings.REGEX_REPLACE_PATTERN)

    def run(self):
        try:
            DependenciesValidator(self.__args.main_file_path, self.__regex_matcher).validate()
            with open(self.__args.destination_file_path, "w") as output_file_descriptor:
                with open(self.__args.main_file_path, "r") as input_file_descriptor:
                    FileWriter(input_file_descriptor, output_file_descriptor, self.__regex_matcher).write()
        except AppException as ex:
            print("Error: %s" % str(ex))


if __name__ == "__main__":
    EmbedMarkdownTool().run()
