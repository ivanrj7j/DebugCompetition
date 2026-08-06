def longest_substring(s: str) -> int:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """
    char_set = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1

        char_set.add(s[r])
        res = max(res, r - l + 1)

    return res