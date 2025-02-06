def longestConsecutive(nums):
    consecutive = []
    result = 0

    for number in sorted(set(nums)):

        if not consecutive or number - consecutive[-1] == 1:
            consecutive.append(number)
        else:
            consecutive = [number]

        current_length = len(consecutive)
        if result < current_length:
            result = current_length

    return result
