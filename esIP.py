def completa8bit(strbin):
    b = strbin[2:]
    l = len(b)
    return "0" * (8 - l) + b


def main():
    address = "10.172.15.92"
    groups = address.split(".")
    groups = [int(group) for group in groups]
    print(groups)
    groups_bin = [bin(group) for group in groups] #all'inizio stampa con 0b per indicare che è una stringa binaria
    print(groups_bin)
    print(completa8bit(groups_bin[1]))
    groupsStrbin = [completa8bit(strbin) for strbin in groups_bin]
    print(groupsStrbin)
    print(".ciao.".join(groupsStrbin))

if __name__ == "__main__":
    main()