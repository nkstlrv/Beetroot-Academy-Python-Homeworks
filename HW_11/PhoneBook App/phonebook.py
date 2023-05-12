from pb_functions import search, create, edit, delete

# ---------------------------------------------------------------------------------------------------------------
print("=" * 50)
print(" " * 10, " P H O N E   B O O K")
print("=" * 50)
print(" " * 39, "v0.1  2023")
print("""\n Hello there!
 This is the Phonebook application""")
print("\n What I can do?"
      "\n\n - Create and store contact's phone number and other necessary info;"
      "\n - Find a contact by Number, Name, Surname, Fullname, Address, etc.;"
      "\n - Delete contact;"
      "\n - Change contact's info.")

# Starting or Quiting the application-----------------------------------------------------------------------------
while True:
    try:
        start_quit = int(input("\n Do you want to continue? "
                               "\n CONTINUE --> [1], QUIT --> [2]: "))
    except ValueError:
        print("\n Input Error"
              "\n Use only given numbers to choose")
        continue
    except Exception as error:
        print(f"\n Unexpected error --> {error}"
              "\n Try again")
        continue
    if start_quit == 1:
        print("\n All right! Let's start")
        break
    elif start_quit == 2:
        print("\n Goodbye!"
              " Hope to see you soon")
        quit()

# Program mode choice------------------------------------------------------------------------------------------
while True:
    prog_mode = int(input("\n No you need to choose the Program mode."
                          "\n Here are the options:"
                          "\n\n - Search --> [1]"
                          "\n - Create new contact --> [2]"
                          "\n - Edit contact's info --> [3]"
                          "\n - Delete contact --> [4]"
                          "\n - Quit the program --> [0]"
                          "\n ENTER your answer: "))

    try:
        prog_mode
    except ValueError:
        print("\n Input Error"
              "\n Use only given numbers to choose")
        continue
    except Exception as error:
        print(f"\n Unexpected error --> {error}"
              "\n Try again")
        continue

    # Search mode-------------------------------------------------------------------------------------------------
    if prog_mode == 1:

        while True:
            search_mode = int(input("\n Options of the SEARCH mode:"
                                    "\n\n - By NAME --> [1]"
                                    "\n - By SURNAME --> [2]"
                                    "\n - By FULLNAME --> [3]"
                                    "\n - By TELEPHONE NUMBER --> [4]"
                                    "\n - By CITY --> [5]"
                                    "\n - By STATE --> [6]"
                                    "\n - By COUNTRY --> [7]"
                                    "\n - Quit --> [0]"
                                    "\n ENTER your answer: "))
            try:
                search_mode
            except ValueError:
                print("\n Input Error"
                      "\n Use only given numbers to choose")
                continue
            except Exception as error:
                print(f"\n Unexpected error --> {error}"
                      "\n Try again")
                continue

            if search_mode == 1:
                search.search_name()
                quit()
            elif search_mode == 2:
                search.search_surname()
                quit()
            elif search_mode == 3:
                search.search_fullname()
                quit()
            elif search_mode == 4:
                search.search_number()
                quit()
            elif search_mode == 5:
                search.search_city()
                quit()
            elif search_mode == 6:
                search.search_state()
                quit()
            elif search_mode == 7:
                search.search_country()
                quit()
            elif search_mode == 1101:
                quit()
            else:
                print("\n There no such option")
                continue

    # Create contact mode -----------------------------------------------------------------------------------------
    elif prog_mode == 2:
        print("\n You have chosen CREATE NEW CONTACT mode")
        create.create_contact()
        quit()

    # Edit contact mode ------------------------------------------------------------------------------------------
    elif prog_mode == 3:
        print("\n You have chosen EDIT mode")
        edit.edit_contact()
        quit()

    # Delete contact mode ---------------------------------------------------------------------------------------
    elif prog_mode == 4:
        print("\n You have chosen DELETE mode")
        delete.delete_contact()
        quit()

    # Quit the program
    elif prog_mode == 0:
        print("\n Bye! Hope to see you soon")
        quit()

    else:
        print("\n There no such option")
        continue