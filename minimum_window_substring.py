def minWindow(s, t):
    left = 0
    right = len(t)
    smallest_window = ""

    for i in range(len(s) - len(t) + 1):
        current = s[left:right]
        result = all(char in current for char in t)

        while result is True:
            same_amount = all(current.count(ch) >= t.count(ch) for ch in t)
            if smallest_window == "" or len(smallest_window) > len(current):
                if same_amount:
                    smallest_window = current
                else:
                    if right < len(s):
                        right += 1
                    else:
                        left += 1
                    current = s[left:right]
                    result = all(char in current for char in t)
                    continue

            left += 1

            current = s[left:right]
            result = all(char in current for char in t)

        right += 1

    return smallest_window


print(minWindow("acbba", "aab"))
