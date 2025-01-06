def longestPalindrome(s):
    """
    Finds the longest palindromic substring in a given string.

    Args:
        s: The input string.

    Returns:
        The longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s

    start = 0
    max_len = 1

    for i in range(n):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l
            l -= 1
            r += 1

        # Even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l
            l -= 1
            r += 1

    return s[start:start + max_len]

# Example usage:
print(longestPalindrome("babad"))  # Output: "bab" or "aba"
print(longestPalindrome("cbbd"))   # Output: "bb"
# Add more test cases here
print(longestPalindrome("a"))  # Output: "a"
print(longestPalindrome("ac"))  # Output: "a" or "c"
print(longestPalindrome("bananas")) # Output: "anana"
print(longestPalindrome("racecar")) # Output: "racecar"
print(longestPalindrome("")) #Output ""
print(longestPalindrome("kayak")) # Output: "kayak"
print(longestPalindrome("level")) # Output: "level"
print(longestPalindrome("A man, a plan, a canal: Panama")) # Output: "a man, a plan, a canal: Panama"
print(longestPalindrome("12321")) # Output: "12321"
print(longestPalindrome("12345")) # Output: "1"
print(longestPalindrome(".,")) # Output: "."


