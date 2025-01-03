import nltk

nltk.download('words')

with open("elements.txt") as f: # elements.txt contains all the elements in the periodic table
    elements = f.read().split()

elements = [element.lower() for element in elements]

letters_in_elements = set()

for element in elements:
    for letter in element:
        letters_in_elements.add(letter)

letters_in_elements = sorted(letters_in_elements)

depth = 5

words = set(w.lower() for w in nltk.corpus.words.words())

def check_if_word_can_be_formed(word):
    # tales a word and checks if it can be formed using the elements in the periodic table
    # check length constraints
    if len(word) < depth:
        return False
    if len(word) > depth * 2:
        return False
    # check if word contains an impossible letter
    for letter in word:
        if letter not in letters_in_elements:
            return False
    
    # check if word can be formed using the elements
    # since some elements have 1 letter and some have 2, we need to check all possible combinations
    current = 0
    element_list = []
    def recursive_search(word, current, element_list):
        if current == len(word):
            if len(element_list) == depth:
                return element_list
            return None
        if current + 1 < len(word):
            if word[current:current+2] in elements:
                element_list.append(word[current:current+2])
                result = recursive_search(word, current + 2, element_list)
                if result:
                    return result
                element_list.pop()
        if word[current] in elements:
            element_list.append(word[current])
            result = recursive_search(word, current + 1, element_list)
            if result:
                return result
            element_list.pop()
        return False
    
    result = recursive_search(word, current, element_list)

    if not result:
        return False
    
    score = 0
    for element in elements:
        count = word.count(element)
        if count:
            score += count
    if score > 11:
        print(word, score)
    
    return result

element_lists = []

for word in words:
    element_list = check_if_word_can_be_formed(word)
    if element_list:
        element_lists.append(element_list)

with open("element_lists.txt", "w") as f:
    for element_list in element_lists:
        f.write(" ".join(element_list) + "\n")