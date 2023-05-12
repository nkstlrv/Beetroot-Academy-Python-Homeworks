# Task 1

# The greeting program.

# Make a program that has your name and the current day of the week stored as separate variables and then prints
# a message like this:

# "Good day <name>! <day> is a perfect day to learn some python."
# Note that  <name> and <day> are predefined variables in source code.

# An additional bonus will be to use different string formatting methods for constructing result string.

my_name = "nIKitA"

lang_1 = "python"
lang_2 = "java"
lang_3 = "c#"

from datetime import datetime
import calendar

date_today = datetime.now()
week_today = calendar.day_name[date_today.weekday()]
date_today = str(date_today)
week_today = str(week_today)

print(f"\n Good day, {my_name.lower().title()}! {week_today.title()},\
 of {date_today[0:10]} is a perfect day to learn some {lang_1.title()}", end="!")
