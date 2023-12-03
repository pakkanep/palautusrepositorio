from int_joukko import IntJoukko

def tee_joukko(*luvut):
    joukko = IntJoukko()
    for luku in luvut:
        joukko.lisaa_listaan(luku)
        
    return joukko

def main():
    joukko = tee_joukko(1, 2, 5, 6, 5, 6, 9)
    print(joukko.kokonaisluku_listaksi())
    
    


if __name__ == "__main__":
    main()