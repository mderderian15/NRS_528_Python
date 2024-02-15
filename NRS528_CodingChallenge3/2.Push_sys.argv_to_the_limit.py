# construct a rudimentary Python script that
# takes a series of inputs as a command
# from a .bat file using sys.argv and does something to them
# The rules:
# 1. Minimum of three arguments to be used
# 2. You must do something simple in 15 lines or fewer
# within the Python file
# 3. Print or file generated output should be produced

# import system
import sys

# print arguments from batch file
print("Argument 1 = " + str(sys.argv[1]))
print("Argument 2 = " + str(sys.argv[2]))
print("Argument 3 = " + str(sys.argv[3]))
