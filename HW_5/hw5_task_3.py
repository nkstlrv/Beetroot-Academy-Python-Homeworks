# Task 3
#
# Words combination
#
# Create a program that reads an input string and then creates and
# prints 5 random strings from characters of the input string.
#
# For example, the program obtained the word ‘hello’,
# so it should print 5 random strings(words) that combine characters
#
# 'h', 'e', 'l', 'l', 'o' -> 'hlelo', 'olelh', 'loleh' …
# Tips: Use random module to get random char from string)

import random

while True:

    ur_word = input("\nEnter any word: ")

    if ur_word.isdigit():
        print("\nUse letters only")

    else:

        word_list = [*ur_word]
        print("\nCharacters list --> ", word_list, "\n")
        print("Shuffled words:\n")

        mixed_word_1 = "".join(random.sample(ur_word,len(ur_word)))
        print("1)", mixed_word_1)

        mixed_word_2 = "".join(random.sample(ur_word,len(ur_word)))
        print("2)", mixed_word_2)

        mixed_word_3 = "".join(random.sample(ur_word,len(ur_word)))
        print("3)", mixed_word_3)

        mixed_word_4 = "".join(random.sample(ur_word,len(ur_word)))
        print("4)", mixed_word_4)

        mixed_word_5 = "".join(random.sample(ur_word, len(ur_word)))
        print("5)", mixed_word_5)
        break




