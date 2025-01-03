import random

with open("element_lists.txt", "r") as f:
    element_lists = f.read().split("\n")

element_lists = [element_list.split(" ") for element_list in element_lists]

if "" in element_lists:
    element_lists.remove("")

included_elements = ["o", "s", "n"]

not_included_elements = ["ho", "k", "u", "p", "w", "ge", "es", "si"]

locked_elements = [(4, "n"), (3, "o")]

possible_solutions = []


for element_list in element_lists:
    correct = True
    for element in included_elements:
        if element not in element_list:
            correct = False
            break
    for index, element in locked_elements:
        if element_list[index] != element:
            correct = False
            break
    for element in not_included_elements:
        if element in element_list:
            correct = False
            break
    if correct:
        possible_solutions.append(element_list)

print(possible_solutions)

print(random.choice(possible_solutions))