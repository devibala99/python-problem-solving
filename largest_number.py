# Method 1: Manual iteration (no built-in max)
def largest_manual(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# Method 2: Using built-in max()
def largest_builtin(numbers):
    if not numbers:
        return None
    return max(numbers)


# Method 3: Sorting and picking last element
def largest_by_sorting(numbers):
    if not numbers:
        return None
    sorted_numbers = sorted(numbers)
    return sorted_numbers[-1]


# Method 4: Using reduce()
from functools import reduce

def largest_reduce(numbers):
    if not numbers:
        return None
    return reduce(lambda a, b: a if a > b else b, numbers)


# Driver code
if __name__ == "__main__":
    nums = [3, 9, 2, 7, 11, 4]

    print("Manual method:", largest_manual(nums))
    print("Built-in max():", largest_builtin(nums))
    print("Using sorting:", largest_by_sorting(nums))
    print("Using reduce():", largest_reduce(nums))
