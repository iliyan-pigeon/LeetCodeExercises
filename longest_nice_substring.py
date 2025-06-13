class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        substrings = [s]
        results = []

        while substrings:
            for index, sb in enumerate(substrings):
                for i, ch in enumerate(sb):
                    if ch.isupper():
                        if chr(ord(ch)+32) not in sb:
                            substrings.pop(index)

                            substrings.append(sb[:i])
                            substrings.append(sb[i+1:])
                            break
                    elif ch.islower():
                        if chr(ord(ch)-32) not in sb:
                            substrings.pop(index)

                            substrings.append(sb[:i])
                            substrings.append(sb[i + 1:])
                            break
                else:
                    if sb not in results and sb != "":
                        results.append(sb)
                    else:
                        substrings.pop(index)

        result = sorted(results, key=len) if results else ""

        max_length = len(result[-1])

        result = sorted([i for i in result if len(i) == max_length])[0] if results else ""

        return result
