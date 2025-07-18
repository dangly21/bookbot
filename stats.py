def num_words(text):
    words = text.split()
    return len(words)

def num_chars(text):
    char = text.lower()
    char_dict = {}
    for char in char:
        if char not in char_dict:
            char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

def sort_on(item):
    return item["num"]

def sort_list(char_dict):
    sort_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            sort_list.append({"char": char, "num": count})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
