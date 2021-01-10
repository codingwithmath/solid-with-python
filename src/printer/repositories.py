from models.repositories import Repositories

class Printer(object):

    def __init__(self, repositories):
        self._repositories = repositories

    def print_repositories(self):
        for repository in self._repositories:
            repository_info = Repositories(repository["id"], repository["name"], repository["stargazers_count"])
            print(repository_info)