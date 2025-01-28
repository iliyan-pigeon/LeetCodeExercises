def findSubstring(s, words):
    word_length = len(words[0])
    all_words_length = len("".join(words))
    starting_points = []

    for i in range(len(s) - all_words_length + 1):
        current = s[i:i+all_words_length]
        current_list = []

        for j in range(0, len(current), word_length):
            word = current[j:j+word_length]
            if word in words:
                current_list.append(word)

        if sorted(current_list) == sorted(words):
            starting_points.append(i)

    return starting_points
