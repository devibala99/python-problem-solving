"""
A collection of methods to count the frequency of elements in a list
using different techniques.
"""


def frequency_loop(nums: list) -> dict:
    """Count frequencies using a manual loop."""
    freq = {}
    for n in nums:
        if n in freq:
            freq[n] += 1
        else:
            freq[n] = 1
    return freq


def frequency_dict_get(nums: list) -> dict:
    """Count frequencies using dictionary get() method."""
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    return freq


def frequency_dict_comprehension(nums: list) -> dict:
    """Count frequencies using dictionary comprehension."""
    return {n: nums.count(n) for n in set(nums)}


def frequency_counter(nums: list) -> dict:
    """Count frequencies using collections.Counter."""
    from collections import Counter
    return dict(Counter(nums))


if __name__ == "__main__":
    sample = [10, 20, 10, 30, 20, 10, 40]

    print("Original List:", sample)
    print("Loop Method:", frequency_loop(sample))
    print("Dict get() Method:", frequency_dict_get(sample))
    print("Dict Comprehension Method:", frequency_dict_comprehension(sample))
    print("Counter Method:", frequency_counter(sample))
