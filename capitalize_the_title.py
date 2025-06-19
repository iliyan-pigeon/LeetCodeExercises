class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = []

        for word in title.split(" "):
            if len(word) <= 2:
                result.append("".join([i.lower() for i in word]))
            else:
                result.append("".join([word[i].upper() if i == 0 else word[i].lower() for i in range(len(word))]))

        return " ".join(result)
