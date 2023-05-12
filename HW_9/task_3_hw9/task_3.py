# Task 3
#
# Basics, import, work with os module
#
# Write a program that counts lines and characters in a file
# (similar to `wc` Unix-utility, for additional info about it follow the link:
# https://www.geeksforgeeks.org/wc-command-linux-examples/
# or in case you have macOS or Linux - just call manual for this utility via command: `man wc`).
#
#  Create a Python module called `mymod.py`, which has three functions:
#
# count_lines(name) function that reads an input file and counts the number of lines in it
# (hint: file.readlines() does most of the work for you, and `len` does the rest)
#
# count_chars(name) function that reads an input file and counts the number of characters in it
# (hint: file.read() returns a single string)
#
# test(name) function that calls both counting functions with a given input file name.
#
# Such a filename generally might be passed-in, hard-coded, input with raw_input,
# or pulled from a command-line via the sys.argv list; for now, assume it’s a passed-in function argument.
# All three `mymod.py` functions should expect a filename string to be passed in.
#
# Test your module interactively, using import and name qualification to fetch your exports.
#
# Does your PYTHONPATH need to include the directory where you created mymod.py?
#
# Try running your module on itself: e.g., test("mymod.py").
# Note that the test opens the file twice;
# if you’re feeling ambitious,
# you may be able to improve this by passing an open
# file object into the two count functions (hint: file.seek(0) is a file rewind).

import sys

print("\n Haven't really understood what I am expected to do in the part with PYPATH and further..."
      "\n Definitely, if we exclude paths of sys.path list, import doesn't work \n")

# sys.path[:] = []

from mymod import count_lines, count_chars
from mymod import test

count_lines("test_file.txt")

count_chars("test_file.txt")

test()
