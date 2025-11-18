def length_of_longest_substring(s: str) -> int:
    """
    Finds the length of the longest substring without repeating characters.

    Args:
        s: The input string.

    Returns:
        The length of the longest substring without duplicates.
    """
    # 1. Initialize variables
    charSet = set()  # Set to store characters in the current window [l, r]
    l = 0            # Left pointer of the sliding window
    maxLength = 0    # Stores the maximum length found so far

    # 2. Iterate (Move the Right Pointer 'r')
    for r in range(len(s)):
        # 3. Check for Duplicates (Window Contraction)
        # If the character at 'r' is already in the set, 
        # contract the window from the left ('l') until the duplicate is removed.
        while s[r] in charSet:
            charSet.remove(s[l]) # Remove the character at the left pointer
            l += 1               # Slide the left pointer one position to the right

        # 4. Expand the Window
        # The window is now valid (no duplicates). Add the new character at 'r'.
        charSet.add(s[r])

        # 5. Update Max Length
        # The current length is r - l + 1
        maxLength = max(maxLength, r - l + 1)

    return maxLength

# --- Test Examples ---

# Example 1: Input: s = "abcabcbb" -> Output: 3 ("abc")
input1 = "abcabcbb"
result1 = length_of_longest_substring(input1)
print(f"Input: \"{input1}\" -> Output: {result1}")

# Example 2: Input: s = "bbbbb" -> Output: 1 ("b")
input2 = "bbbbb"
result2 = length_of_longest_substring(input2)
print(f"Input: \"{input2}\" -> Output: {result2}")

# Example 3: Input: s = "pwwkew" -> Output: 3 ("wke" or "kew")
input3 = "pwwkew"
result3 = length_of_longest_substring(input3)
print(f"Input: \"{input3}\" -> Output: {result3}")

# Example 4: Input: s = "" -> Output: 0
input4 = ""
result4 = length_of_longest_substring(input4)
print(f"Input: \"{input4}\" -> Output: {result4}")

# Example 5: Input: s = "dvdf" -> Output: 3 ("vdf")
input5 = "dvdf"
result5 = length_of_longest_substring(input5)
print(f"Input: \"{input5}\" -> Output: {result5}")
