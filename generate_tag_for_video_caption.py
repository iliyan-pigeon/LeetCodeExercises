class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.strip().split(" ")

        result = "#"
        result += caption[0].lower()

        for i in range(1, len(caption)):
            result += caption[i].capitalize()

        return result[:100]
