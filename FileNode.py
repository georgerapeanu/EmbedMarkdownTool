import os
import re

from Exceptions import FileNodeException


class FileNode:
    """ This class parses a file given by its path and builds its dependencies.
        This is only used in order to check if all the referenced file exists and to search circular dependencies.

    """
    def __init__(self, file_path, regex_matcher):
        """ Constructor for FileNode object.

        :param file_path: the path of the file
        :type file_path: str
        :param regex_matcher: a compiled regex that matches the replace pattern
        :type regex_matcher: re.Pattern
        :raises FileNodeException: if the file does not exist.
        """
        if not os.path.exists(file_path):
            raise FileNodeException("File %s does not exist" % file_path)
        self.__dependencies = []
        self.__file_path = file_path
        with open(file_path) as f:
            for line in f:
                for dependency in regex_matcher.findall(line):
                    self.__dependencies.append(dependency)

    @property
    def dependencies(self):
        return self.__dependencies

    @property
    def file_path(self):
        return self.__file_path
