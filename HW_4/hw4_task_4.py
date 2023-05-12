u_name = "Nikita"

while True:

    login = str(input("Enter your user name: "))
    login = login.rstrip(" ").title()

    if login == u_name:
        print("Welcome!")
        break

    elif login.isdigit():
        print("Use letters only")

    else:
        print("Incorrect. Try again")
        continue


