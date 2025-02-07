class Solution(object):
    def isValid(self, s):
        brackets_stack = []
        result = True
        brackets = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in brackets.values():
                brackets_stack.append(bracket)
                continue

            if not brackets_stack:
                result = False
                break
            elif brackets[bracket] != brackets_stack.pop():
                result = False
                break

        if brackets_stack:
            result = False

        return result

