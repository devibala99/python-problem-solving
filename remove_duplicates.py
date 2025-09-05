"""
A collection of methods to remove duplicates from a list using different techniques.
"""


def remove_duplicates_loop(nums: list) -> list:
    """Remove duplicates manually using a loop."""
    unique = []
    for n in nums:
        if n not in unique:
            unique.append(n)
    return unique


def remove_duplicates_set(nums: list) -> list:
    """Remove duplicates using a set (order not guaranteed)."""
    return list(set(nums))


def remove_duplicates_set_ordered(nums: list) -> list:
    """Remove duplicates using a set while preserving order."""
    seen = set()
    unique = []
    for n in nums:
        if n not in seen:
            seen.add(n)
            unique.append(n)
    return unique


def remove_duplicates_dict(nums: list) -> list:
    """Remove duplicates using dict.fromkeys() (preserves order)."""
    return list(dict.fromkeys(nums))


def remove_duplicates_list_comprehension(nums: list) -> list:
    """Remove duplicates using list comprehension + set tracking."""
    seen = set()
    return [x for x in nums if not (x in seen or seen.add(x))]


if __name__ == "__main__":
    sample = [1, 2, 2, 3, 4, 4, 5, 1, 6]

    print("Original List:", sample)
    print("Loop Method:", remove_duplicates_loop(sample))
    print("Set Method (Unordered):", remove_duplicates_set(sample))
    print("Set Method (Ordered):", remove_duplicates_set_ordered(sample))
    print("Dict.fromkeys Method:", remove_duplicates_dict(sample))
    print("List Comprehension Method:", remove_duplicates_list_comprehension(sample))
