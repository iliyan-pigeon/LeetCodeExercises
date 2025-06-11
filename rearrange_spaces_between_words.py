class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = []
        current_word = ""
        spaces = 0

        for ch in text:
            if ch == " ":
                spaces += 1

                if current_word != "":
                    words.append(current_word)
                    current_word = ""
            else:
                current_word += ch

        if current_word != "":
            words.append(current_word)

        between = spaces // (len(words)-1)
        after = spaces % (len(words)-1)

        return f"{' '*between}".join(words) + " "*after
