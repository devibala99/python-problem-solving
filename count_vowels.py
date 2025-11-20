"""
A collection of methods to count vowels in a string using different techniques.
"""

VOWELS = "aeiouAEIOU"


def count_vowels_loop(s: str) -> int:
    """Count vowels using a simple loop."""
    count = 0
    for ch in s:
        if ch in VOWELS:
            count += 1
    return count


def count_vowels_list_comprehension(s: str) -> int:
    """Count vowels using list comprehension."""
    return sum([1 for ch in s if ch in VOWELS])


def count_vowels_filter(s: str) -> int:
    """Count vowels using filter() function."""
    return len(list(filter(lambda ch: ch in VOWELS, s)))


def count_vowels_set(s: str) -> int:
    """Count vowels efficiently using a set for faster lookup."""
    vowels_set = set(VOWELS)
    return sum(1 for ch in s if ch in vowels_set)


if __name__ == "__main__":
    sample = "Hello Python Programming"

    print("Original:", sample)
    print("Loop Method:", count_vowels_loop(sample))
    print("List Comprehension:", count_vowels_list_comprehension(sample))
    print("Filter Function:", count_vowels_filter(sample))
    print("Set Method:", count_vowels_set(sample))
