class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, license, authors):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.license = license
        self.authors = authors

    def _stringify_dependencies(self, list):
        string = ""
        for a in list:
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
