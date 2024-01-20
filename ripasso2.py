lettere = "abcdefghilmnopqrstuvz"
N = len(lettere)
lettere2numeri = {}
numeri2lettere = {}
for pos, lettera in enumerate(lettere):
    lettere2numeri[lettera] = pos
    numeri2lettere[pos] = lettera
testo_chiaro = "parola"
chiave = "itisdelpozzo"
testo_criptato = ""
for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave):
    # print(lettere2numeri[lettera_testo], lettere2numeri[lettera_chiave]) 
    numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera_chiave]) % 21
    testo_criptato += numeri2lettere[numero]

for lettera_testo, lettera_chiave in zip():
    # print(lettere2numeri[lettera_testo], lettere2numeri[lettera_chiave]) 
    numero = (lettere2numeri[lettera_testo] - lettere2numeri[lettera_chiave]) % 21
    



