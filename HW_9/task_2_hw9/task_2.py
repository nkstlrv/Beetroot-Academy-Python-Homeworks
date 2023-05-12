# Task 2
#
# The sys module.
#
# The “sys.path” list is initialized from the PYTHONPATH environment variable.
# Is it possible to change it from within Python?
# If so, does it affect where Python looks for module files?
# Run some interactive tests to find it out.

from sys import path

print("\n First of all let's get all directories where interpreter finds modules and functions")

print("\n", path)

print("\n We've got a list of strings made of paths."
      "\n The first one is a directory of our current module"
      "\n -->", path[0])

print("\n Now let's import function from another module")

from imprt_test import pypath_test

pypath_test()

print("\n Let's try to change sys.path list")

path.insert(0, "Pypath list changed successfully")

print("\n So we can see that list has successfully been changed" 
      "\n\n", path)

print("\n Now lat's try to make our list empty")

path[:] = []

print("\n Our new sys.path list is -->", path)

print("\n Let's call imported function again")

pypath_test()

print("\n So despite the change of sys.path list, import still working!")