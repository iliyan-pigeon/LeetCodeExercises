class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        sentence_sum = sum([ord(ch) for ch in set(sentence)])

        return sentence_sum == 2847
