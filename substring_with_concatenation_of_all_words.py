# Solution 1
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


# Solution 2
from collections import Counter


class Solution(object):
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_length = len(words[0])
        word_count = len(words)
        substring_length = word_length * word_count
        word_frequency = Counter(words)
        result = []

        for i in range(word_length):
            left = i
            right = i
            current_count = Counter()
            while right + word_length <= len(s):

                word = s[right:right + word_length]
                right += word_length
                if word in word_frequency:
                    current_count[word] += 1

                    while current_count[word] > word_frequency[word]:
                        current_count[s[left:left + word_length]] -= 1
                        left += word_length

                    if right - left == substring_length:
                        result.append(left)
                else:

                    current_count.clear()
                    left = right
        return result

