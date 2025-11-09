from collections import defaultdict


def longest_subarray(the_word):
    longest = 0
    left = 0
    right = 1
    length = len(the_word)

    while right <= length:
        current = the_word[left:right]

        if len(set(current)) == len(current):
            right += 1

            if len(current) > longest:
                longest = len(current)

        else:
            left += 1

    return longest


print(longest_subarray(["a", "b", "c", "d", "b", "e", "a"]))


def longest_subarray(s):
    longest = 0
    l = 0
    counter = defaultdict(int)

    for r in range(len(s)):
        counter[s[r]] += 1

        while counter[s[r]] > 1:
            l += 1
            counter[s[l]] -= 1

        longest = max(longest, r - l + 1)

    return longest


print(longest_subarray(["a", "b", "c", "d", "b", "e", "a"]))

