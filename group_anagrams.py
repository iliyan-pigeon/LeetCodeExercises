def groupAnagrams(strs):
    anagrams = [[]]

    for word in strs:
        word_added = False

        for anagram in anagrams:
            if not anagram or sorted(word) == sorted(anagram[0]):
                anagram.append(word)
                word_added = True

        if not word_added:
            anagrams.append([word])

    return anagrams
