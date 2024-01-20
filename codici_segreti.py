"""
# cifrario di vernam

fare una classe Testo le cui istanze possano contenere
sia un testo in chiaro sia un testo codificato
parametri: stringa, chiave, bool per sapere se è codificato o no
metodi: cifra() decifra()
"""

d_chiave_lettera = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7,
        "i": 8,
        "l": 9,
        "m": 10,
        "n": 11,
        "o": 12,
        "p": 13,
        "q": 14,
        "r": 15,
        "s": 16,
        "t": 17,
        "u": 18,
        "v": 19,
        "z": 20,
}

d_lettera_chiave = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
    8: "i",
    9: "l",
    10: "m",
    11: "n",
    12: "o",
    13: "p",
    14: "q",
    15: "r",
    16: "s",
    17: "t",
    18: "u",
    19: "v",
    20: "z"
}

class Testo():
    def __init__(self, stringa, chiave, codificato) -> None:
        self.stringa = stringa
        self.chiave = chiave
        self.codificato = codificato

    def cifra(self):
        if not self.codificato:
            cod = str([d_lettera_chiave[char] for char in self.stringa])
            
            #return (self.stringa + self.chiave) % 21
    
    def decifra(self):
        if self.codificato:
            #return (self.stringa + self.chiave) % 21
            pass


def main():
    #testo = Testo("ciao", "abcd", False)
    print(str([i for i in range(10)]))


if __name__ == "__main__":
    main()