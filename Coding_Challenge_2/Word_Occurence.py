input_string = 'hi dee hi how are you mr dee'
# split the string into word lists
w = input_string.split()
print(w)
print(f'"hi" appears {w.count("hi")} time(s)')
print(f'"dee" appears {w.count("dee")} time(s)')
print(f'"how" appears {w.count("how")} time(s)')
print(f'"are" appears {w.count("are")} time(s)')
print(f'"you" appears {w.count("you")} time(s)')
print(f'"mr" appears {w.count("mr")} time(s)')

for word in w:
    count = w.count(word)
    print(word + " " + str(count))