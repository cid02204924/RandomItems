def hybrid_merge_sort(array):
    # Threshold where insertion sort is faster
    INSERTION_SORT_THRESHOLD = 10

    if len(array) <= INSERTION_SORT_THRESHOLD:
        return insertion_sort(array)

    middle_index = len(array) // 2
    left_half = hybrid_merge_sort(array[:middle_index])
    right_half = hybrid_merge_sort(array[middle_index:])

    return merge_arrays(left_half, right_half)


def insertion_sort(array):
    sorted_array = array.copy()
    for current_index in range(1, len(sorted_array)):
        key = sorted_array[current_index]
        previous_index = current_index - 1
        while previous_index >= 0 and sorted_array[previous_index] > key:
            sorted_array[previous_index + 1] = sorted_array[previous_index]
            previous_index -= 1
        sorted_array[previous_index + 1] = key
    return sorted_array


def merge_arrays(left_array, right_array):
    sorted_array = []
    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            sorted_array.append(left_array[left_index])
            left_index += 1
        else:
            sorted_array.append(right_array[right_index])
            right_index += 1

    sorted_array.extend(left_array[left_index:])
    sorted_array.extend(right_array[right_index:])
    return sorted_array


# Example usage
if __name__ == "__main__":
    sample_data = [38, 27, 43, 3, 9, 82, 10, 4, 5, 0, 99, 1]
    print("Original array:", sample_data)
    sorted_result = hybrid_merge_sort(sample_data)
    print("Sorted array:", sorted_result)
