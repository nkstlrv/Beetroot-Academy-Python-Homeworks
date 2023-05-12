def count_lines(name: str):
    with open(name) as txt_file:
        lines = txt_file.readline()
        total_lines = len(lines)
        print("\n There are -", total_lines, "- total lines in your .txt file")


def count_chars(name: str):
    with open("test_file.txt") as txt_file:
        chars = txt_file.read()
        total_chars = len(chars)
        print("\n There are -", total_chars, "- total characters in your .txt file")


def test():

    while True:
        name = input("\n Please, ENTER your file name in a given format"
                     "\n Example --> file.txt: ")
        try:
            count_lines(name)
            count_chars(name)
            break

        except FileNotFoundError:
            print("\n File not found. Try again")
            continue


# -----------------------------------------------------------------------------------

# Functions test:

if __name__ == "__main__":
    count_lines("test_file.txt")
    count_chars("test_file.txt")
    test()
