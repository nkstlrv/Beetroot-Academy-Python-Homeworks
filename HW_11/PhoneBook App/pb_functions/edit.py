import json

PHONEBOOK_FILE = "HW_11\PhoneBook App\phonebook.json" 


def edit_contact():
    with open(PHONEBOOK_FILE, "r") as pb1:
        phone_book1 = json.load(pb1)
    # Searchin contact by number
    contact_dict = {}
    i = 0
    while True:
        number = input("\n Please, enter contact's number: ")

        for contact in phone_book1:
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

    # Choosing which parameter to edit
    while True:
        try:
            edit_info = int(input("\n Which info do you want to edit?"
                                  "\n\n - NAME --> [1]"
                                  "\n - SURNAME --> [2]"
                                  "\n - TELEPHONE NUMBER --> [3]"
                                  "\n - CITY --> [4]"
                                  "\n - STATE --> [5]"
                                  "\n - COUNTRY --> [6]"
                                  "\n ENTER your answer: "))
        except ValueError:
            print("\n Input Error"
                  "\n Use only given numbers to choose")
            continue
        except Exception as error:
            print(f"\n Unexpected error --> {error}"
                  "\n Try again")
            continue

        # Changing contact's Name
        if edit_info == 1:

            name = input("\n ENTER contacts new NAME: ").title()

            while True:

                try:
                    next_step = int(input("\n Do you want to save results?"
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
                    break
                elif next_step == 2:
                    quit()

            contact_dict["Name"] = name
            new_dict = contact_dict
            phone_book1.remove(contact)
            phone_book1.append(new_dict)

            with open(
                    PHONEBOOK_FILE, "w") as npb:
                json.dump(phone_book1, npb)
                quit()

        # Changing contact's Surname
        if edit_info == 2:

            surname = input("\n ENTER contacts new SURNAME: ").title()

            while True:

                try:
                    next_step = int(input("\n Do you want to save results?"
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
                    break
                elif next_step == 2:
                    quit()

            contact_dict["Surname"] = surname
            new_dict = contact_dict
            phone_book1.remove(contact)
            phone_book1.append(new_dict)

            with open(
                    PHONEBOOK_FILE, "w") as npb:
                json.dump(phone_book1, npb)
                quit()

        # Changing contact's Phone number
        if edit_info == 3:

            ph_num = input("\n ENTER contacts new PHONE NUMBER: ")

            while True:

                try:
                    next_step = int(input("\n Do you want to save results?"
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
                    break
                elif next_step == 2:
                    quit()

            contact_dict["Number"] = ph_num
            new_dict = contact_dict
            phone_book1.remove(contact)
            phone_book1.append(new_dict)

            with open(
                    PHONEBOOK_FILE, "w") as npb:
                json.dump(phone_book1, npb)
                quit()

        # Changing contact's City
        if edit_info == 4:

            city = input("\n ENTER contacts new CITY: ").title()

            while True:

                try:
                    next_step = int(input("\n Do you want to save results?"
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
                    break
                elif next_step == 2:
                    quit()

            contact_dict["City"] = city
            new_dict = contact_dict
            phone_book1.remove(contact)
            phone_book1.append(new_dict)

            with open(
                    PHONEBOOK_FILE, "w") as npb:
                json.dump(phone_book1, npb)
                quit()

        # Changing contact's State
        if edit_info == 5:

            state = input("\n ENTER contacts new STATE: ")

            while True:

                try:
                    next_step = int(input("\n Do you want to save results?"
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
                    break
                elif next_step == 2:
                    quit()

            contact_dict["State"] = state
            new_dict = contact_dict
            phone_book1.remove(contact)
            phone_book1.append(new_dict)

            with open(
                    PHONEBOOK_FILE, "w") as npb:
                json.dump(phone_book1, npb)
                quit()

        # Changing contact's Country
        if edit_info == 6:

            country = input("\n ENTER contacts new COUNTRY: ")

            while True:

                try:
                    next_step = int(input("\n Do you want to save results?"
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
                    break
                elif next_step == 2:
                    quit()

            contact_dict["Country"] = country
            new_dict = contact_dict
            phone_book1.remove(contact)
            phone_book1.append(new_dict)

            with open(
                    PHONEBOOK_FILE, "w") as npb:
                json.dump(phone_book1, npb)
                quit()



# Functions test ------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    edit_contact()
