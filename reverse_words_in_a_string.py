class Solution(object):
    def reverseWords(self, s):
        s = " ".join(i for i in reversed(s.strip(" ").split(" ")) if i != "")
    
        return s
