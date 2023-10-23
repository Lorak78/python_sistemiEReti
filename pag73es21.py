def rimuoviVocali(string):
    vocali = "aeiouAEIOU"
    stringNoVoc = [char for char in string if char in vocali]
    return stringNoVoc

def main():
    string = "ciao a tutti"
    print(string)
    string = rimuoviVocali(string)
    print("$".join(string))

def main1():
    string = "ciao a tutti"
    print(string)
    string = rimuoviVocali(string)
    print(string)

if __name__ == "__main__":
    main()