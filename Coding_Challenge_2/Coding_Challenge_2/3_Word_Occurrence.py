# 3. Given a single phrase, count the occurrence of each word
# Using this string:
#
# string = 'hi dee hi how are you mr dee'
# Count the occurrence of each word, and print the word plus the count
# (hint, you might want to "split" this into a list by a white space: " ").

input_string = 'hi dee hi how are you mr dee'
# split the string into word lists
w = input_string.split()

for word in w:
    count = w.count(word)
    print(word + " " + "appears" + " " + str(count) + " " + "time(s)")