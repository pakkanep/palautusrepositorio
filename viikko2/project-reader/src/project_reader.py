from urllib import request
from project import Project
import toml



class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        uusi = toml.loads(content)

        name = uusi["tool"]["poetry"]["name"]
        description = uusi["tool"]["poetry"]["description"]
        dependencies = uusi["tool"]["poetry"]["dependencies"]
        dev_dependencies = uusi["tool"]["poetry"]["group"]["dev"]["dependencies"]
        uusi_license = uusi["tool"]["poetry"]["license"]
        authors = uusi["tool"]["poetry"]["authors"]


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name,
                       description,
                       dependencies,
                       dev_dependencies,
                       uusi_license,
                       authors)
