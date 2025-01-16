class Solution(object):
    def strStr(self, haystack, needle):
        if needle not in haystack:
            return -1

        result = ""
        needle_length = len(needle)

        for i in range(len(haystack)):
            if i + needle_length <= len(haystack):
                if haystack[i:(i + needle_length)] == needle:
                    result = i
                    break

        return result
