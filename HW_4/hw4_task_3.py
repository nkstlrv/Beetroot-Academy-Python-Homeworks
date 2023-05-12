a = 3

b = 5

correct_answer = (a + b) * (b - a)
print(correct_answer)

while True:

    user_input = input(f"Solve the math problem: (a + b) * (b - a), if a = {a}, and b = {b}: ")
    user_answer = float(user_input)

    if user_answer == correct_answer:
        print("Well done! :)")
        break

    else:
        print("Wrong :(")





