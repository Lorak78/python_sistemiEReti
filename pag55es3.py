def main():
    prima = 5
    seconda = 7
    print(f"prima: {prima} seconda: {seconda}")
    prima, seconda = seconda, prima
    print(f"prima: {prima} seconda: {seconda}")


if __name__ == "__main__":
    main()