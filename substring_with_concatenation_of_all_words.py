def findSubstring(s, words):
    word_length = len(words[0])
    all_words_length = len("".join(words))
    words_amount = len(words)
    starting_points = []

    for i in range(0, len(s) - all_words_length + 1, word_length):
        current = s[i:i+all_words_length]
        current_list = set()
        left = 0
        right = word_length

        for j in range(words_amount):
            current_list.add(current[left:right])
            left += word_length
            right += word_length

        if current_list == set(words):
            starting_points.append(i)

    return starting_points


print(findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
