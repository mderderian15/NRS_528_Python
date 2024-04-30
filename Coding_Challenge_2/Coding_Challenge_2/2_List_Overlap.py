# 2. List overlap
# Using these lists:
#
# list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
# list_b = ['dog', 'hamster', 'snake']
# Determine which items are present in both lists.
# Determine which items do not overlap in the lists.

# Determine which items are present in both lists
#list overlap determination which items are in both lists
list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']
intersected_list = []
for animal in list_a:
    if animal in list_b:
        intersected_list.append(animal)
print(intersected_list)

# Determine which items do not overlap in the lists
#list elements that do not overlap in both lists
no_overlap_list = []
for animal in list_a:
    if not animal in list_b:
        print(animal)
