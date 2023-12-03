KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0

    def luku_kuuluu_listaan(self, n):
        if n in self.lukujono:
            return True
        else:
            return False

    def kasvata_listaa(self):
        self.lukujono = self.lukujono + self._luo_lista(OLETUSKASVATUS)

    def lisaa_listaan(self, n):
        if n not in self.lukujono[:self.alkioiden_lkm]:
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                self.kasvata_listaa()
            return True

        return False
    

    def poista(self, n):
        if self.luku_kuuluu_listaan(n):
            indeksi = self.lukujono.index(n)
            self.lukujono.pop(indeksi)
            self.lukujono.append(0)
            self.alkioiden_lkm -= 1
            return True

        return False

    def kopioi_lista(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def listan_koko(self):
        return self.alkioiden_lkm

    def kokonaisluku_listaksi(self):
        return self.lukujono[:self.alkioiden_lkm]


    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.kokonaisluku_listaksi()
        b_taulu = b.kokonaisluku_listaksi()

        for i in range(0, len(a_taulu)):
            x.lisaa_listaan(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa_listaan(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        palautus = IntJoukko()
        a_taulu = a.kokonaisluku_listaksi()
        b_taulu = b.kokonaisluku_listaksi()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    palautus.lisaa_listaan(b_taulu[j])

        return palautus

    @staticmethod
    def erotus(a, b):
        palautus = IntJoukko()
        a_taulu = a.kokonaisluku_listaksi()
        b_taulu = b.kokonaisluku_listaksi()
        lisays_lista = [i for i in a_taulu if i not in b_taulu]
        for alkio in lisays_lista:
            palautus.lisaa_listaan(alkio)
        return palautus

   
    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"

        if self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"

        else:
            elements_str = ", ".join(map(str, self.lukujono[:self.alkioiden_lkm]))
            return f"{{{elements_str}}}"
