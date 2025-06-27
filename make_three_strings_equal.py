class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        min_length = min(len(s1), len(s2), len(s3))

        operations = 0

        while len(s1) > min_length or len(s2) > min_length or len(s3) > min_length:
            if len(s1) > min_length:
                s1 = s1[:-1]
                operations += 1
            if len(s2) > min_length:
                s2 = s2[:-1]
                operations += 1
            if len(s3) > min_length:
                s3 = s3[:-1]
                operations += 1

        while len({s1, s2, s3}) != 1:
            s1 = s1[:-1]
            s2 = s2[:-1]
            s3 = s3[:-1]
            operations += 3

            if "" in (s1, s2, s3):
                return -1

        return operations
