class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n < 1000:
            return str(n)

        else:
            n = list(str(n))
            n.insert(-3, ".")

            return "".join(n)
