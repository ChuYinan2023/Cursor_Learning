def lengthOfLongestSubstring(s: str) -> int:
    char_map = {}  # Stores the last index of each character
    left = 0       # Left pointer of the sliding window
    max_len = 0    # Maximum length found
    
    for right, char in enumerate(s):
        # If character is already in the map and within the current window
        if char in char_map and char_map[char] >= left:
            # Move the left pointer to the right of the previous occurrence
            left = char_map[char] + 1
        
        # Update the last index of the character
        char_map[char] = right
        
        # Update the maximum length if needed
        max_len = max(max_len, right - left + 1)
    
    return max_len