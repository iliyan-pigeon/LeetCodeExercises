def lengthOfLongestSubstring(s):
    longest = s
    filtered_s = ""
    left = 0
    right = len(s)
    counter = 0

    while len(filtered_s) != longest:
        longest = s[left:right]
        filtered_s = set(longest)
        if counter % 2 == 0:
            left += 1
        elif counter % 2 != 0:
            right += 1
        counter += 1

    return longest


print(lengthOfLongestSubstring("abcabcbb"))
