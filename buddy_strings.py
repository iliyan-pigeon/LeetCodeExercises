class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        first = None
        second = None

        for i in range(len(s)):
            if s[i] in goal:
                first = i

                for j in range(i + 1, len(s)):
                    if s[j] in goal:
                        second = j

                        new_s = s[:first]+s[second]+s[first+1:second]+s[first]+s[second+1:]

                        if new_s == goal:
                            return True

        return False
