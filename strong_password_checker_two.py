class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        criteria_met = []

        special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
        previous_character = ""

        for ch in password:
            if ch == previous_character:
                return False

            previous_character = ch

            if ch.islower() and "L" not in criteria_met:
                criteria_met.append("L")
            elif ch.isupper() and "U" not in criteria_met:
                criteria_met.append("U")
            elif ch.isnumeric() and "D" not in criteria_met:
                criteria_met.append("D")
            elif ch in special_characters and "S" not in criteria_met:
                criteria_met.append("S")

        return len(criteria_met) == 4
