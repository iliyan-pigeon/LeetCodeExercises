class Solution:
    def generateTag(self, caption: str) -> str:
        caption = caption.split(" ")

        result = "#"
        result += caption[0].lower()

        for i in range(1, len(caption)):
            result += f"{caption[i][0].upper()}{caption[i][1:].lower()}"

        return result[:101]
