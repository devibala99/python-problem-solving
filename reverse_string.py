"""
Collection of methods to reverse string using different techniques.
"""
text = "hello world"

def reverse_using_loop(s: str) -> str:
    """Reverse a string manually using a for-loop."""
    reverse_str = ""
    for ch in s:
        reverse_str = ch + reverse_str # add character at the front
    return reverse_str

def reverse_using_slicing(s: str) -> str:
    """Reverse a string using Python slicing."""
    return s[::-1]

def reverse_using_reversed_function(s: str) -> str:
    """Reverse a string using the built-in reversed() with join."""
    return "".join(reversed(s))

def reverse_using_recursion(s: str) -> str:
    """Reverse a string using recursion."""
    if len(s) <= 1:
        return s
    return s[-1] + reverse_using_recursion(s[:-1])

def reverse_using_two_pointers(s: str) -> str:
    """Reverse a string using two pointers technique."""
    chars = list(s)
    left, right = 0, len(chars)-1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return "".join(chars)

if __name__ == "__main__":
    text = "Hello Universe"
    print("Original string:", text)
    print("Loop:", reverse_using_loop(text))
    print("Slicing:", reverse_using_slicing(text))
    print("Reversed:", reverse_using_reversed_function(text))
    print("Recursion:", reverse_using_recursion(text))
    print("Two-pointers:", reverse_using_reversed_function(text))