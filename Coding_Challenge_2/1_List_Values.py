# 1. List values
# Using this list:
#
# [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
# You need to do two separate things here and report both in your Python file. You
# should have two solutions in this file, one for item 1 and one for item 2. Item 2 is
# tricky so if you get stuck try your best (no penalty), for a hint check out the solution
# by desiato here.
#
# 1. Make a new list that has all the elements less than 5 from this list in it and print out
# this new list.
# 2. Write this in one line of Python (you do not need to append to a list just
# print the output).

# list all values
list_values = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
list_values_less_than_5 = [v for v in list_values if v < 5]
print(list_values_less_than_5)

# writing list values less than 5 in one string
print([v for v in list_values if v<5])

for number in list_values:
    if number < 5:
        print(number)