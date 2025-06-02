def merge_sort(arr):
    # Base case: if the array has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare elements from both halves and build the sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are any remaining elements in left or right, append them
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    
    return sorted_array


# Run the merge sort algorithm
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", data)
    sorted_data = merge_sort(data)
    print("Sorted array:", sorted_data)
