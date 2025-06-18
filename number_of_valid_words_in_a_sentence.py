class Solution:
    def countValidWords(self, sentence: str) -> int:
        valid_count = 0

        sentence = sentence.split(" ")

        for word in sentence:
            if word == "":
                continue

            hyphens = False
            punctuations = False
            valid = True

            for i, ch in enumerate(word):
                if ch.isnumeric():
                    valid = False
                    break
                elif ch == "-":
                    if hyphens:
                        valid = False
                        break
                    elif i == 0 or i == len(word)-1:
                        valid = False
                        break
                    elif word[i-1] in ["!", ".", ","] or word[i+1] in ["!", ".", ","]:
                        valid = False
                        break
                    else:
                        hyphens = True
                elif ch in ["!", ".", ","] and i != len(word)-1:
                    valid = False
                    break

            if valid:
                valid_count += 1

        return valid_count
