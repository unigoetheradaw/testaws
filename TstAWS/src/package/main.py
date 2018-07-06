def main():
    print("Hallo World")
    with open("test.txt", "w") as f:
        f.write("hi")

if __name__ == "__main__":
    main()