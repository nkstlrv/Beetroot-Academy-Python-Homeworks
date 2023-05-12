# Task 1
#
# Write a function called oops that explicitly raises an IndexError exception when called.
# Then write another function that calls oops inside a try/except statement to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

from my_functios.oops_functios import try_oops

# oops_functios.oops()

try_oops()

print("\n So if we just replace IndexError with KeyError inside except: part,"
      "\n exception won't work because the error that occurs in oops function is IndexError,"
      "\n KeyError works with dictionaries"
      "\n However, if we add raise KeyError at the end independently of except IndexError:"
      "\n program will rise KeyError even if it is not occurred.")