class Sovelluslogiikka:
    def __init__(self, arvo=0):
        self.arvohistoria = [0]
        self._arvo = arvo

    def kumoa(self):
        if len(self.arvohistoria) < 1:
            pass
        else:
            self._arvo = self.arvohistoria.pop()

    def miinus(self, operandi: int):
        self.arvohistoria.append(self._arvo)
        self._arvo = self._arvo - operandi

    def plus(self, operandi: int):
        self.arvohistoria.append(self._arvo)
        self._arvo = self._arvo + operandi

    def nollaa(self):
        self.arvohistoria.append(self._arvo)
        self._arvo = 0

    def aseta_arvo(self, arvo):
        self.arvohistoria.append(self._arvo)
        self._arvo = arvo

    def arvo(self):
        return self._arvo
