import json
PHONEBOOK_FILE = "HW_11\PhoneBook App\phonebook.json" 

with open(PHONEBOOK_FILE, "r") as pb:
    phone_book = json.load(pb)


# Search by Name
def search_name() -> str:
    n_lst = []
    while True:

        name = input("\n Please enter contact's NAME: ").title()

        for contact in phone_book:
            if contact["Name"] == name:
                n_lst.append(contact["Number"])
        if len(n_lst) == 0:
            print("\n There is no contact with this name")
            continue
        else:
            print(f"\n {name}'s phone number is --> {n_lst[0]}")
            break


# Search by Surname
def search_surname() -> str:
    s_lst = []
    while True:

        surname = input("\n Please enter contact's SURNAME: ").title()

        for contact in phone_book:
            if contact["Surname"] == surname:
                s_lst.append(contact["Number"])
        if len(s_lst) == 0:
            print("\n There is no contact with this name")
            continue
        else:
            print(f"\n {surname}'s phone number is --> {s_lst[0]}")
            break


# Search by Fullname
def search_fullname() -> str:
    fn_lst = []
    while True:

        c_name = input("\n Firstly, enter contact's NAME: ").title()
        c_surname = input("\n Now, enter contact's SURNAME: ").title()

        for contact in phone_book:
            if contact["Surname"] == c_surname:
                if contact["Name"] == c_name:
                    fn_lst.append(contact["Number"])
        if len(fn_lst) == 0:
            print("\n There is no contact with this name")
            continue
        else:
            print(f"\n {c_name}", f"{c_surname}'s phone number is --> {fn_lst[0]}")
            break


# Search by Telephone number
def search_number() -> str:
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
            print("\n Here is contact's info:\n")
            for key, val in contact_dict.items():
                print("", f"{key} -- {val}")
            break


# Search by City:
def search_city() -> str:
    city_lst = []
    while True:

        city = input("\n Please enter contact's CITY: ").title()

        for contact in phone_book:
            if contact["City"] == city:
                city_lst.append(contact["Number"])
        if len(city_lst) == 0:
            print("\n There is no contact living in this city")
            continue
        else:
            print(f"\n Contact's phone number is --> {city_lst[0]}")
            break


# Search by State
def search_state() -> str:
    state_lst = []
    while True:

        state = input("\n Please enter contact's STATE: ")

        for contact in phone_book:
            if contact["State"] == state:
                state_lst.append(contact["Number"])
        if len(state_lst) == 0:
            print("\n There is no contact living in this state")
            continue
        else:
            print(f"\n Contact's phone number is --> {state_lst[0]}")
            break


# Search by Country
def search_country() -> str:
    country_lst = []
    while True:

        country = input("\n Please enter contact's COUNTRY: ")

        for contact in phone_book:
            if contact["Country"] == country:
                country_lst.append(contact["Number"])
        if len(country_lst) == 0:
            print("\n There is no contact living in this Country")
            continue
        else:
            print(f"\n Contact's phone number is --> {country_lst[0]}")
            break


# --------------------------------------------------------------
# Functions test:
if __name__ == "__main__":
    search_country()