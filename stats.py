def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars(text):
    allchars = {}
    for t in text:
        ch = t.lower()
        if ch not in allchars:
           allchars[ch] = 1
        else: 
            allchars[ch] += 1
    return allchars

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list