import json

PHONEBOOK_FILE = "HW_11\PhoneBook App\phonebook.json" 

def delete_contact():
    with open(PHONEBOOK_FILE, "r") as pb:
        phone_book = json.load(pb)
    # Searchin contact by number
    contact_dict = {}
    i = 0
    while True:
        number = input("\n Please, enter contact's number: ")
        for contact in phone_book:
            if number == contact["Number"]:
                contact_dict = contact
                break
            else:
                continue
        if contact_dict == {}:
            print("\n There is NO contact with this number")
            continue
        else:
            for key, val in contact_dict.items():
                print("", f"{key} -- {val}")
            break

    while True:
        try:
            next_step = int(input("\n Do you want to DELETE this contact?"
                                  "\n Yes --> [1] No --> [2]: "))
        except ValueError:
            print("\n Input Error"
                  "\n Use only given numbers to choose")
            continue
        except Exception as error:
            print(f"\n Unexpected error --> {error}"
                  "\n Try again")
            continue

        if next_step == 1:
            phone_book.remove(contact_dict)
            with open(
                    PHONEBOOK_FILE, "w") as pb:
                json.dump(phone_book, pb)
                quit()
        elif next_step == 2:
            quit()


# Functions test ------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    delete_contact()
