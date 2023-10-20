#SLICING DI STRINGHE
s = "ciao come stai?"
# =  0  1  2  3
# = -4 -3 -2 -1
print(f"Il primo carattere è: {s[0]}")
print(f"L'ultimo carattere è: {s[-1]}")
print(f"Il penultimo carattere è: {s[-2]}")
#C-style NON USARE
print(f"L'ultimo carattere è: {s[len(s)-1]}")

print(f"dal carattere in posizione 3 incluso al carattere in posizione 7 escluso: {s[3:7]}")
print(f"tutta la stringa esclusi primo ed ultimo carattere: {s[1:-1]}")
print(f"tutta la stringa escluso il primo carattere: {s[1:]}")
print(f"tutta la stringa: {s[:]}")

print(s[::-1]) #stampa tutta la stringa al contrario