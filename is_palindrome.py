# Palindrome Challenge

def is_palindrome(s):
    # Normalize: lowercase and remove spaces
    normalized = ''.join(c.lower() for c in s if c.isalnum())
    # Compare string to its reverse
    return normalized == normalized[::-1]

# Test examples
print(is_palindrome("racecar"))                  # True
print(is_palindrome("hello"))                    # False
print(is_palindrome("A man a plan a canal Panama"))  # True