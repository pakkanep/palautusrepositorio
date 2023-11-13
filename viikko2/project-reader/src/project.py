class Project:
    def __init__(self, name, dependencies, licenses, authors):
        self.name = name[0]
        self.description = name[1]
        self.dependencies = dependencies[0]
        self.dev_dependencies = dependencies[1]
        self.license = licenses
        self.authors = authors


    def return_info(self):
        infolist = [
            self.name,
            self.description,
            self.dependencies,
            self.dev_dependencies,
            self.license,
            self.authors
        ]
        return infolist

    def _stringify_dependencies(self, lista):
        string = ""
        for a in lista:
            string += "- "+a+"\n"
        return string

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}"
            f"\n"
            f"\nAuthors:"
            f"\n{self._stringify_dependencies(self.authors)}"
            f"\nDependencies:"
            f"\n{self._stringify_dependencies(self.dependencies)}"
            f"\nDevelopment dependencies:"
            f"\n{self._stringify_dependencies(self.dev_dependencies)}"
        )
