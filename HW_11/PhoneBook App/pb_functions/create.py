import json

PHONEBOOK_FILE = "HW_11\PhoneBook App\phonebook.json" 


def create_contact():
    # Phone number
    while True:

        phone_num = input("\n Firstly, lets add your contact's PHONE NUMBER"
                          "\n Acceptable formats: [0772074849] and [+490772074748]"
                          "\n ENTER your answer: ")
        if len(phone_num) in range(8, 15):
            print(f"\n Your new contact's number is --> {phone_num}")

            try:
                next_step = int(input("\n Do you want to continue?"
                                      "\n Yes --> [1] No --> [2] Quit --> [0]: "))
            except ValueError:
                print("\n Input Error"
                      "\n Use only given numbers to choose")
                continue
            except Exception as error:
                print(f"\n Unexpected error --> {error}"
                      "\n Try again")
                continue

            if next_step == 1:
                break
            elif next_step == 2:
                continue
            elif next_step == 0:
                quit()

    # Name and Surname
    while True:
        name = input("\n Now, add contact's NAME"
                     "\n ENTER your answer: ").title()
        surname = input("\n And SURNAME"
                        "\n ENTER your answer: ").title()
        print(f"\n Your contact's full name is {name} {surname}")

        try:
            next_step = int(input("\n Do you want to continue?"
                                  "\n Yes --> [1] No --> [2] Quit --> [0]: "))
        except ValueError:
            print("\n Input Error"
                  "\n Use only given numbers to choose")
            continue
        except Exception as error:
            print(f"\n Unexpected error --> {error}"
                  "\n Try again")
            continue

        if next_step == 1:
            break
        elif next_step == 2:
            continue
        elif next_step == 0:
            quit()

    # Address
    while True:
        city = input("\n Finally let's add contact's ADDRESS"
                     "\n ENTER contact's CITY: ").title()
        state = input("\n Now ENTER contact's STATE: ")
        country = input("\n And finally ENTER contact's COUNTRY: ")
        print(f"\n Your contact's address is --> {city}, {country}, {state}")

        try:
            next_step = int(input("\n Do you want to continue?"
                                  "\n Yes --> [1] No --> [2] Quit --> [0]: "))
        except ValueError:
            print("\n Input Error"
                  "\n Use only given numbers to choose")
            continue
        except Exception as error:
            print(f"\n Unexpected error --> {error}"
                  "\n Try again")
            continue

        if next_step == 1:
            break
        elif next_step == 2:
            continue
        elif next_step == 0:
            quit()

    new_cont = {
        "Number": phone_num,
        "Name": name,
        "Surname": surname,
        "City": city,
        "State": state,
        "Country": country
    }



    for key, val in new_cont.items():
        print("", f"{key} -- {val}")
        
    while True:
        try:
            next_step = int(input("\n Do you want to SAVE this contact?"
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

            with open(PHONEBOOK_FILE,
                    "r") as opb:
                old_book = json.load(opb)

            old_book.append(new_cont)

            with open(PHONEBOOK_FILE, "w") as npb:
                json.dump(old_book, npb)
            quit()
        elif next_step == 2:
            quit()


# ----------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    create_contact()
