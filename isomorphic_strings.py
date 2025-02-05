class Solution(object):
    def isIsomorphic(self, s, t):
        mapping = {}
        result = True

        for i in range(len(s)):
            if s[i] not in mapping:
                if t[i] not in mapping.values():
                    mapping[s[i]] = t[i]
                else:
                    result = False
                    break
            elif s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    result = False
                    break

        return result
