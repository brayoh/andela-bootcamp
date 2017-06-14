def words(words):
    words_list = words.split(" ")
    words_count = {}
    for word in words_list:
        count = 0
        if word in words_count:
            count = words_count[word]
            words_count[word] = count + 1
        else:
            words_count[word] = count + 1

    return words_count


# print(words("brian brian is : awesome"))
