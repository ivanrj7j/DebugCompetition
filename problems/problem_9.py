def find_anagrams(s: str, p: str) -> list[int]:
    """
    Given two strings s and p, return an array of all the start indices of p's 
    anagrams in s. You may return the answer in any order.

    Examples:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]
    Explanation:
    The substring with start index = 0 is "cba", which is an anagram of "abc".
    The substring with start index = 6 is "bac", which is an anagram of "abc".

    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    Explanation:
    The substring with start index = 0 is "ab", which is an anagram of "ab".
    The substring with start index = 1 is "ba", which is an anagram of "ab".
    The substring with start index = 2 is "ab", which is an anagram of "ab".
    """
    ns, np = len(s), len(p)

    if not p:
        return []

    if ns < np:
        return []

    p_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1

    s_count = {}
    res = []

    l = 0

    for r in range(ns):
        # Add the new character
        s_count[s[r]] = s_count.get(s[r], 0) + 1

        # Shrink window if it becomes too large
        if r - l + 1 > np:
            s_count[s[l]] -= 1
            if s_count[s[l]] == 0:
                del s_count[s[l]]
            l += 1

        # Compare only when window size is exactly np
        if r - l + 1 == np and s_count == p_count:
            res.append(l)

    return res