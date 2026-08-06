def longest_substring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.

    Examples:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
    """
    last_seen = {}
    start = 0
    longest = 0

    for end, char in enumerate(s):
        if char in last_seen and last_seen[char] >= start:
            start = last_seen[char] + 1
        last_seen[char] = end
        longest = max(longest, end - start + 1)

    return longest
