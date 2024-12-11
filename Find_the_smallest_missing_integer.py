def find_smallest_missing_positive(nums):
    """
    Finds the smallest missing positive integer from an unsorted list of integers.

    Parameters:
        nums (list of int): An unsorted list of integers.

    Returns:
        int: The smallest positive integer that is missing from the list.

    Algorithm:
    1. Filter the list to retain only positive numbers.
    2. Use a set to efficiently check for missing integers in the range [min(nums), max(nums)].
    3. If no missing integer is found in the range, return max(nums) + 1.
    """
    # Filter to include only positive numbers
    nums = [num for num in nums if num > 0]
    if not nums:
        return 1  # If there are no positive numbers, return 1

    # Find the range of interest
    nums_set = set(nums)
    smallest = min(nums)
    largest = max(nums)

    # Check for the first missing number in the range [smallest, largest]
    for i in range(smallest, largest + 1):
        if i not in nums_set:
            return i

    # If all numbers in the range are present, return the next integer
    return largest + 1

# Test cases
print(find_smallest_missing_positive([3, 4, -1, 1]))  # Output: 2 (Missing positive integer is 2)
print(find_smallest_missing_positive([1, 2, 0]))      # Output: 3 (Missing positive integer is 3)
print(find_smallest_missing_positive([7, 8, 9, 11 ])) # Output: 10 (Smallest positive integer missing is 10)
