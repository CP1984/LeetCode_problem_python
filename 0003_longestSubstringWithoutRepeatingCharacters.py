class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_char_set = set()  # Set to store unique characters in current window
        start = 0  # Starting index of the window
        end = 0  # Ending index of the window

        max_length = 0  # Initialize max_length to 0 to handle empty string case
        total_length = len(s)  # Length of the input string

        while end < total_length:
            if s[end] not in unique_char_set:
                unique_char_set.add(s[end])  # Add current character to set
                max_length = max(max_length, len(unique_char_set))  # Update max_length
                end += 1  # Move the end pointer to the right
            else:
                unique_char_set.remove(s[start])  # Remove the starting character from set
                start += 1  # Move the start pointer to the right

        return max_length

if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("abcdef", 6),
        ("abba", 2),
        ("aab", 2),
        ("dvdf", 3),
        ("tmmzuxt", 5),
        ("abcdaefga", 7)
    ]

    solution = Solution()
    for s, expected in test_cases:
        ans = solution.lengthOfLongestSubstring(s)
        print(f"Input string: '{s}', Answer: {ans}, Expected: {expected}")
