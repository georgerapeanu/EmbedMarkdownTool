class FileWriter:
    """ This class is responsible for writing the final file, supposing the given one has a valid dependency graph

    """
    def __init__(self, source_file_descriptor, destination_file_descriptor, regex_matcher):
        """ Constructor for a file writer instance

        :param source_file_descriptor: the source file from which it parses the text
        :param destination_file_descriptor: The destination file to which it writes
        :param regex_matcher: the regex matcher
        :type regex_matcher: re.Pattern
        """
        self.__source_file_descriptor = source_file_descriptor
        self.__destination_file_descriptor = destination_file_descriptor
        self.__regex_matcher = regex_matcher

    def write(self):
        """ Processes the current file

        :return: None
        """
        for line in self.__source_file_descriptor:
            if self.__regex_matcher.search(line) is not None:
                span = self.__regex_matcher.search(line).span()
                for i in range(0, span[0]):
                    self.__destination_file_descriptor.write(line[i])
                with open(self.__regex_matcher.findall(line)[0], "r") as f:
                    FileWriter(f, self.__destination_file_descriptor, self.__regex_matcher).write()
                for i in range(span[1], len(line)):
                    self.__destination_file_descriptor.write(line[i])
            else:
                self.__destination_file_descriptor.write(line)
