"""
A collection of methods to find the second largest number in a list
using different techniques.
"""


def second_largest_sorted(nums: list) -> int:
    """Find the second largest number using sorting."""
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        raise ValueError("List must contain at least two distinct numbers.")
    unique_nums.sort()
    return unique_nums[-2]


def second_largest_loop(nums: list) -> int:
    """Find the second largest number using a manual loop."""
    if len(nums) < 2:
        raise ValueError("List must contain at least two numbers.")

    largest = second = float("-inf")

    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif largest > n > second:
            second = n

    if second == float("-inf"):
        raise ValueError("List must contain at least two distinct numbers.")

    return second


def second_largest_builtin(nums: list) -> int:
    """Find the second largest using max() and removing the largest."""
    if len(nums) < 2:
        raise ValueError("List must contain at least two numbers.")

    largest = max(nums)
    filtered = [n for n in nums if n != largest]

    if not filtered:
        raise ValueError("List must contain at least two distinct numbers.")

    return max(filtered)


if __name__ == "__main__":
    sample = [10, 20, 4, 20, 8, 15]

    print("Original List:", sample)
    print("Sorted Method:", second_largest_sorted(sample))
    print("Loop Method:", second_largest_loop(sample))
    print("Built-in Method:", second_largest_builtin(sample))
