u_name = input("Enter your name: ")
input_string = u_name


if len(input_string) > 2:
    print(f"Output string is --> {input_string[:2]}" f"{input_string[-2:]}")

elif len(input_string) == 2:
    print(f"Output string is --> {input_string * 2}")

else:
    print("")
















