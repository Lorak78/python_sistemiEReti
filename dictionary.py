def main():
    #il dizionario è una collezione di coppie chiave:valore
    #il dizionario non ha indici ma si indicizza per chiave
    #chiave deve essere univoca
    lista = ["ciao", 2, 1, "c"]
    dizionario = {"nome": "Mario", "cognome": "Rossi"} #con le graffe, la chiave deve essere di un solo tipo
    #chiave:valore/"nome":"Mario"
    print(dizionario["nome"])
    dizionario["data nascita"] = "01/01/1900" #aggiunge un nuovo elemento al dizionario
    dizionario["età"] = 123#aggiungo
    dizionario["nome"] = "luca"#sovrascrivo l'elemento con chiave "nome"
    print(dizionario)

    #ciclo for su dizionario 1
    for chiave in dizionario:
        print(f"chiave: {chiave} valore: {dizionario[chiave]}")

    rubrica = {3358043859: "Mario Rossi", 3950594051: "Alice Verdi"}
    for chiave in rubrica:
        print(f"chiave: {chiave} valore: {rubrica[chiave]}")



if __name__ == "__main__":
    main()