from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        operations = 0

        for op in logs:
            if op == "../" and operations > 0:
                operations -= 1
            elif op != "./":
                operations += 1

        return operations
