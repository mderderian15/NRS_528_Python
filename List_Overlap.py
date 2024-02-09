#list overlap determination which items are in both lists
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
intersected_list = []
for animal in list_a:
    if animal in list_b:
        intersected_list.append(animal)
print(intersected_list)

#list elements that do not overlap in both lists
print(set(list_a) ^ set(list_b))



