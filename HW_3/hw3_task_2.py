# Task 2

# Manipulate strings.

# Save your first and last name as separate variables, then use string concatenation to add them together
# with a white space in between and print a greeting.

my_first_name = "nIKitA"
my_second_name = "vaILotS"

lang_1 = "python"
lang_2 = "java"
lang_3 = "c#"

from datetime import datetime
import calendar

date_today = datetime.now()
week_today = calendar.day_name[date_today.weekday()]
date_today = str(date_today)
week_today = str(week_today)

print(f"\n Good day, {my_first_name.lower().title()}" + " " + f"{my_second_name[::-1].lower().title()}!"
f"\n {week_today.title()}" f",of {date_today[0:10]} is a perfect day to learn some {lang_1.title()}", end="!")

# Without (+ " " +)

print(f"\n \n Good day, {my_first_name.lower().title()} {my_second_name[::-1].lower().title()}!"
f"\n {week_today.title()}" f",of {date_today[0:10]} is a perfect day to learn some {lang_1.title()}", end="!")