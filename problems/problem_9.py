def find_anagrams(s: str, p: str) -> list[int]:
    """
    Given two strings s and p, return an array of all the start indices of p's
    anagrams in s. You may return the answer in any order.

    Examples:
    Input: s = "cbaebabacd", p = "abc"
    Output: [0,6]

    Input: s = "abab", p = "ab"
    Output: [0,1,2]
    """
    ns, np = len(s), len(p)

    if np == 0:
        return []

    if ns < np:
        return []

    p_count = {}
    s_count = {}

    for c in p:
        p_count[c] = p_count.get(c, 0) + 1

    res = []

    for i in range(ns):
        s_count[s[i]] = s_count.get(s[i], 0) + 1

        if i >= np:
            left = s[i - np]
            s_count[left] -= 1
            if s_count[left] == 0:
                del s_count[left]

        if s_count == p_count:
            res.append(i - np + 1)

    return res