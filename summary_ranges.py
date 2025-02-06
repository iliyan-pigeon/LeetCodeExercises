class Solution(object):
    def summaryRanges(self, nums):
        ranges = []
        current = ""
        first_number = None
        last_number = None

        for number in nums:
            if first_number is None:
                first_number = number
                last_number = number
                current = str(first_number)

            elif abs(number - last_number) == 1:
                last_number = number

                current = str(first_number) + "->" + str(last_number)

            else:
                ranges.append(current)
                first_number = number
                last_number = number
                current = str(first_number)

        if current not in ranges and current != "":
            ranges.append(current)

        return ranges
