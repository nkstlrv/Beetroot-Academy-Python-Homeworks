while True:

    ph_num = input("Enter your Phone number. Format -- [0123456789, without +38]: ")

    if ph_num.isalpha():
        print("Numbers only")
        continue
    elif len(ph_num) != 10:
        print("Must contain 10 digits")
        continue

    if len(ph_num) == 10:
        if ph_num.isdigit():
            print(f"Welcome! Your number is --> +38{ph_num}")
            break





    # if len(ph_num) == 10:
    #     if ph_num.isdigit():
    #         print("welcome!".title())
    #         break
    #
    # if ph_num.isalpha():
    #     print("NUMBERS only")
    #     continue
    # if len(ph_num) != 10:
    #     print("Must contain 10 digits")
