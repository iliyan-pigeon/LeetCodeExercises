# Solution 1
class Solution(object):
    def minWindow(self, s, t):
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


from collections import defaultdict


# Solution 2
class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        # Frequency map for characters in t
        target_counts = defaultdict(int)
        for ch in t:
            target_counts[ch] += 1

        required = len(target_counts)
        left = right = 0
        formed = 0
        window_counts = defaultdict(int)

        # Tuple to store the minimum window details (length, left, right)
        min_window = (float('inf'), 0, 0)

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            # Check if current character's count in the window meets the target
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1

            # Try to contract the window once all characters are formed
            while left <= right and formed == required:
                current_length = right - left + 1
                # Update the minimum window if a smaller valid window is found
                if current_length < min_window[0]:
                    min_window = (current_length, left, right)

                # Move left pointer to try a smaller window
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in target_counts and window_counts[left_char] < target_counts[left_char]:
                    formed -= 1
                left += 1

            right += 1

        # Return the smallest window or empty string if not found
        return s[min_window[1]:min_window[2] + 1] if min_window[0] != float('inf') else ""


    print(minWindow("acbba", "aab"))
