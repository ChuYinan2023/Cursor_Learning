from longest_substring import lengthOfLongestSubstring  # 导入函数

def test_longest_substring():
    test_cases = [
        ("abcabcbb", 3),       # Example 1
        ("bbbbb", 1),          # Example 2
        ("pwwkew", 3),         # Example 3
        ("", 0),               # Empty string
        ("abcdefg", 7),        # All unique characters
        ("aab", 2),            # Repeated characters at start
        ("abba", 2),           # Repeated characters with window movement
        ("tmmzuxt", 5),        # Complex case with multiple repeats
        ("1234567890", 10),    # Numbers
        ("!@#$%^&*()", 10),    # Special characters
        ("abcdeedcba", 5),     # Palindrome with unique substring
        ("a" * 10000, 1),      # Large input with single character
        ("a" * 10000 + "b", 2) # Large input with two characters
    ]
    
    for i, (input_str, expected) in enumerate(test_cases):
        result = lengthOfLongestSubstring(input_str)  # 调用 lengthOfLongestSubstring 函数
        assert result == expected, f"Test case {i+1} failed: input='{input_str}', expected={expected}, got={result}"
        print(f"Test case {i+1} passed:  result={result}")
    
    print("All test cases passed!")

# Run the tests
test_longest_substring()