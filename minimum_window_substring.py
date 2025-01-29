def minWindow(s, t):
    left = 0
    right = len(t)
    smallest_window = ""

    for i in range(len(s) - len(t) + 1):
        current = s[left:right]
        result = all(char in current for char in t)

        while result is True:
            if smallest_window == "" or len(smallest_window) > len(current):
                smallest_window = current

            left += 1

            current = s[left:right]
            result = all(char in current for char in t)

        right += 1

    return smallest_window


print(minWindow("aa", "aa"))
