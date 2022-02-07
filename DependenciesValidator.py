from Exceptions import AppException, DependenciesValidatorException, FileNodeException
from FileNode import FileNode


class DependenciesValidator:
    """ This class is responsible for validating that no circular dependencies exist
        Given a start file and the appropriate regex matcher, it checks that there are no circular dependencies.
    """

    def __run_file_search(self, file_node):
        """ This function runs a DFS algorithm to find all reachable files given a starting file node

        :param file_node: the starting file node
        :type file_node: FileNode
        :return: None
        """
        self.__processed_files[file_node.file_path] = file_node
        self.__in_degree[file_node.file_path] = 0
        for dependency in file_node.dependencies:
            if dependency in self.__processed_files:
                continue
            try:
                dependency_node = FileNode(dependency, self.__regex_matcher)
                self.__run_file_search(dependency_node)
                self.__in_degree[dependency_node.file_path] += 1
            except FileNodeException as ex:
                self.__errors.append("%s\n Referenced here %s" % (str(ex), file_node.file_path))

    def __run_topological_sort(self):
        """ This is a standard topological sort used in order to check for circular dependencies

        :return: None
        """
        order = []
        for file_path in self.__processed_files.keys():
            if self.__in_degree[file_path] == 0:
                order.append(file_path)

        idx = 0

        while idx < len(order):
            for dependency in self.__processed_files[order[idx]].dependencies:
                self.__in_degree[dependency] -= 1
                if self.__in_degree[dependency] == 0:
                    order.append(dependency)
            idx += 1

        if len(self.__processed_files.keys()) != len(order):
            self.__errors.append("There exist circular imports")

    def __init__(self, main_file_path, regex_matcher):
        """ Constructor for DependenciesValidator.

        :param main_file_path: the path to the main markdown file
        :type main_file_path: str
        :param regex_matcher: the appropriate regex matcher for the pattern to be replaced in the files
        :type regex_matcher: re.Pattern
        :raises DependenciesValidatorException: If files do not exist or if there is a circular dependency
        """
        self.__processed_files = {}
        self.__in_degree = {}
        self.__regex_matcher = regex_matcher
        self.__errors = []
        self.__main_file_path = main_file_path

    def validate(self):
        """ Validates the dependency graph
        Also, it indirectly checks that all files exist(FileNode checks this and it uses FileNode).
        It first parses all files which can be accessed directly or indirectly by following the dependency graph.
        And then it tries to run a topological sort on the graph.
        If it fails, then there exists a circular dependency

        :raises DependenciesValidatorException: if the dependency graph is invalid
        :return: None
        """
        try:
            main_file_node = FileNode(self.__main_file_path, self.__regex_matcher)
            self.__run_file_search(main_file_node)
            self.__run_topological_sort()
            if len(self.__errors) > 0:
                raise DependenciesValidatorException("\n".join(self.__errors))
        except AppException as ex:
            raise DependenciesValidatorException(str(ex))
