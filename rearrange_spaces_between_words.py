# Solution 1
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

        if len(words) > 1:
            between = spaces // (len(words)-1) if spaces else 0
            after = spaces % (len(words)-1) if spaces else 0
        else:
            between = 0
            after = spaces

        return f"{' '*between}".join(words) + " "*after


# Solution 2
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        cnt = len(words)
        spaces = text.count(' ')
        gap = 0 if cnt == 1 else spaces // (cnt - 1)

        trailing_spaces = spaces - gap * (cnt - 1)
        return (' ' * gap).join(words) + ' ' * trailing_spaces
