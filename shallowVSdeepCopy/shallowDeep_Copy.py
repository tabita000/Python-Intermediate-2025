"""This program shows that a shallow copy still shares the inside lists, so if you change something in the shallow copy, it changes the original too. A deep copy makes a totally separate version, so changes don’t affect the original."""

import copy

fruits = [["apple", "banana"], ["ornge","grape"]]

shallow = copy.copy(fruits)
deep = copy.deepcopy(fruits)

shallow[0][1] = "shallow mango"

deep[1][0] = "deep peach"

print("")
print("original:", fruits)
print("Shallow:", shallow)
print("Deep:", fruits)