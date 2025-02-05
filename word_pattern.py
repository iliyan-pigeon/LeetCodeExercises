class Solution(object):
    def wordPattern(self, pattern, s):
        mapping = {}
        words = s.split(" ")
        result = True

        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in mapping:
                if words[i] in mapping.values():
                    result = False
                    break
                else:
                    mapping[pattern[i]] = words[i]
            elif pattern[i] in mapping:
                if mapping[pattern[i]] != words[i]:
                    result = False
                    break

        return result 