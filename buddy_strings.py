class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        first = None
        second = None

        # Check for length mismatch
        if len(s) != len(goal):
            return False

        # If strings are identical, check for at least one duplicate character
        if s == goal:
            return len(set(s)) < len(goal)

        for i in goal:
            if first is None and i in s:
                first = s.index(i)
            elif i in s:
                second = i.index(i, first+1)

                if first > second:
                    second, first = first, second

                s_new = s[:first]+s[second]+s[first+1:second]+s[first]+s[second+1:]

                if s_new == goal:
                    return True

        return False
