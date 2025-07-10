class Solution:
    def concatHex36(self, n: int) -> str:
        def int_to_base36(number):
            if number < 0:
                raise ValueError("Number must be non-negative")

            if number == 0:
                return "0"

            base36_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            result = []

            while number > 0:
                number, remainder = divmod(number, 36)
                result.append(base36_chars[remainder])

            # Reverse the result since we've been appending the least significant digit
            return ''.join(reversed(result))

        hexadecimal = hex(n*n)[2:]
        hexatrigesimal = int_to_base36(n**3)

        return f"{hexadecimal}{hexatrigesimal}"
