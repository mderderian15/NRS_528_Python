# 4. User input
# Ask the user for an input of their current age,
# and tell them how many years until they reach retirement (65 years old).
#
# Hint:
#
# age = input("What is your age? ")
# print "Your age is " + str(age)

# Create input for user's age
age = int(input("What is your age? "))

# Create value for years left until retirement
retire_in = 65 - age

print ("Your age is " + str(age))
print("You are " + str(retire_in) + " years away from retirement")
