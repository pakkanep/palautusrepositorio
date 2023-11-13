from urllib.request import urlopen
from contextlib import closing
import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        with closing(urlopen(self._url)) as response:
            content = response.read().decode("utf-8")
        uusi = toml.loads(content)
        return self.handle_info(uusi)

    def handle_info(self, uusi):
        name = uusi["tool"]["poetry"]["name"]
        description = uusi["tool"]["poetry"]["description"]
        dependencies = uusi["tool"]["poetry"]["dependencies"]
        dev_dependencies =uusi["tool"]["poetry"]["group"]["dev"]["dependencies"]
        uusi_license = uusi["tool"]["poetry"]["license"]
        authors = uusi["tool"]["poetry"]["authors"]

        return Project((name, description),
                    (dependencies, dev_dependencies),
                    uusi_license,
                    authors)
