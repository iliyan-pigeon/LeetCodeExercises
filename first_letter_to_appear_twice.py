class Solution:
    def repeatedCharacter(self, s: str) -> str:
        appeared = ""

        for ch in s:
            if ch in appeared:
                return ch

            appeared += ch
