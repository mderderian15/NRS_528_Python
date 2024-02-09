# list all values
list_values = [1, 2, 3, 6, 8, 12, 20, 32, 46, 85]
list_values_less_than_5 = [v for v in list_values if v < 5]
print(list_values_less_than_5)

# writing list values less than 5 in one string
print([v for v in list_values if v<5])
