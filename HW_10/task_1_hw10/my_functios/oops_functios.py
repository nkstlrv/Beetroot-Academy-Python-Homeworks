
def oops():
    usr_input_1 = input("\n Create your list"
                        "\n ENTER numbers separated by coma: ")
    usr_list = usr_input_1.split(",")
    print(usr_list)

    # Try to enter index out of range to call an IndexError
    usr_input_2 = int(input("\n Now, ENTER an index of an item in a list to see what it is: "))
    print(usr_list[usr_input_2])


def try_oops():
    try:
        oops()
    except IndexError:
        print("\n ERROR"
              "\n Your index is out of list's range")
    # raise KeyError


# _____________________________________________________
# Functions test:

if __name__ == "__main__":
    # oops()
    try_oops()