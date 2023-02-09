def find_duplicate(nums):
    numbers = sorted(nums)

    if len(numbers) < 2:
        return False

    for index in range(len(numbers) - 1):
        if not isinstance(numbers[index], int) or numbers[index] < 0:
            return False
        elif numbers[index] == numbers[index + 1]:
            return numbers[index]

    return False
