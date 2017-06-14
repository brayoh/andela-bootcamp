import re

def words(words):
    words_list = words.split()
    words_count = {}
    if isinstance(words, str):
        for word in words_list:
            count = 0
            word = int(word) if re.match('^[0-9]', word) else word
            if word in words_count:
                count = words_count[word]
                words_count[word] = count + 1
            else:
                words_count[word] = count + 1
        return words_count
    else:
        raise TypeError("please provide a string as input")
