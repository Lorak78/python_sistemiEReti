def pretty_print(m, sep = "\t"):
    for riga in m:
        riga_str = [str(x) for x in riga]
        print(sep.join(riga_str))



def mat2d_adiacenze(m):
    return {i: [j for j, n in enumerate(m[i]) if n] for i in range(len(m))}

def main():
    d_adiacenze = {0: [2, 3], 1: [2, 4], 2: [0, 1, 3], 3: [0, 2, 4], 4: [1, 3]}
    #mat = [[0 for _ in d_adiacenze] for _ in d_adiacenze] oppure
    mat = [[0] * len(d_adiacenze) for _ in d_adiacenze]
    for i, riga in enumerate(mat): #oppure for k, v in d_adiacenze.items()
        for j in d_adiacenze[i]:
            riga[j] = 1
    pretty_print(mat, " ")
    print(mat2d_adiacenze(mat))


if __name__ == "__main__":
    main()