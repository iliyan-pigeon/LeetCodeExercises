def find_boundary(arr):
    left, right = 0, len(arr)-1

    while left < right:
        current_index = (left + right) // 2

        if arr[current_index] is True:
            if arr[current_index-1] is False:
                return current_index
            right = current_index - 1
        elif arr[current_index] is False:
            if arr[current_index+1] is True:
                return current_index+1
            left = current_index + 1

    return -1


print(find_boundary([False, False, True, True, True, True, True, True, True, True, True]))


def find_min_rotated(arr):
    left, right = 0, len(arr)-1
    boundary = -1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= arr[-1]:
            boundary = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary


print(find_min_rotated([30, 40, 50, 10, 20]))