"""
A collection of methods to check if a string or number is a palindrome
using different techniques.
"""

def is_palindrome_string_reverse(s: str) -> bool:
    """Check palindrome by reversing the string."""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def is_palindrome_string_two_pointer(s: str) -> bool:
    """Check palindrome using the two-pointer technique."""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def is_palindrome_string_loop(s: str) -> bool:
    """Check palindrome manually using a loop to build reverse."""
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    reverse_str = ""
    for ch in cleaned:
        reverse_str = ch + reverse_str
    return cleaned == reverse_str


def is_palindrome_number(n: int) -> bool:
    """Check palindrome by converting number to string."""
    s = str(n)
    return s == s[::-1]


def is_palindrome_number_math(n: int) -> bool:
    """Check palindrome by reversing digits mathematically."""
    original = n
    reverse_num = 0

    while n > 0:
        reverse_num = reverse_num * 10 + (n % 10)
        n //= 10

    return original == reverse_num


if __name__ == "__main__":
    sample_string = "Madam"
    sample_number = 121

    print("String Palindrome (Reverse Method):", is_palindrome_string_reverse(sample_string))
    print("String Palindrome (Two Pointer):", is_palindrome_string_two_pointer(sample_string))
    print("String Palindrome (Loop Method):", is_palindrome_string_loop(sample_string))

    print("Number Palindrome (String Method):", is_palindrome_number(sample_number))
    print("Number Palindrome (Math Method):", is_palindrome_number_math(sample_number))
