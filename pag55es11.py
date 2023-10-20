def main():
    x = [0, 1, 2, 3, 5, 6, 7, 8]
    meta1 = x[0:int(len(x)/2)]
    meta2 = x[int(len(x)/2):]
    meta1.append(5)
    print(f"{meta1} {meta2}")

if __name__ == "__main__":
    main()