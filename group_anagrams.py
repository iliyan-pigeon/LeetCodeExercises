class Solution(object):
    def groupAnagrams(self, strs):
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


# Solution 2
from collections import defaultdict


def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:

        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())
