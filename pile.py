#LE PILE IN PYTHON
def push(p, elem):
    p.append(elem)

def pop(p):
    x = p.pop()
    return x

def main():
    """pila = [1, 2, 3, 4]
    pila.append(5) #push metodo liste
    print(pila)
    x = pila.pop()#pop metodom liste
    print(pila)
    print(x)"""
    pila = [1, 2, 3, 4]
    push(pila, 10)
    print(pila)
    x = pop(pila)
    print(f"{pila}, {x}")
    

if __name__ == "__main__":
    main()