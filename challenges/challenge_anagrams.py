def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    first_list = list(first_string.lower())
    second_list = list(second_string.lower())

    merge_sort(first_list)
    merge_sort(second_list)

    if first_list == second_list:
        boolean = True
    else:
        boolean = False

    return ("".join(first_list), "".join(second_list), boolean)


def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    l_index, r_index = 0, 0

    for index in range(start, end):
        if l_index >= len(left):
            numbers[index] = right[r_index]
            r_index += 1
        elif r_index >= len(right):
            numbers[index] = left[l_index]
            l_index += 1
        elif left[l_index] < right[r_index]:
            numbers[index] = left[l_index]
            l_index += 1
        else:
            numbers[index] = right[r_index]
            r_index += 1

