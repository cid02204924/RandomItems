def merge_sort(array):
    # Base case: if the array has 0 or 1 element, it's already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    middle_index = len(array) // 2
    left_half = merge_sort(array[:middle_index])
    right_half = merge_sort(array[middle_index:])

    # Merge the sorted halves
    return merge_arrays(left_half, right_half)


def merge_arrays(left_array, right_array):
    sorted_array = []
    left_index = 0
    right_index = 0

    # Compare elements from both arrays and append the smallest to sorted_array
    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] <= right_array[right_index]:
            sorted_array.append(left_array[left_index])
            left_index += 1
        else:
            sorted_array.append(right_array[right_index])
            right_index += 1

    # Append any remaining elements from both arrays
    sorted_array.extend(left_array[left_index:])
    sorted_array.extend(right_array[right_index:])

    return sorted_array


# Example usage
if __name__ == "__main__":
    sample_data = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample_data)
    sorted_result = merge_sort(sample_data)
    print("Sorted array:", sorted_result)