class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        vowels = "aeiou"

        for i, word in enumerate(sentence.split(" ")):
            if word[0].lower() in vowels:
                word += "ma"
            else:
                word = word[1:]+word[0]+"ma"

            word += "a" * (i+1)

            result.append(word)

        return " ".join(result)
