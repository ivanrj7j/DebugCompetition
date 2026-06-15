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
    if ns < np:
        return []
        
    p_count = {}
    s_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1
        
    for i in range(np):
        s_count[s[i]] = s_count.get(s[i], 0) + 1
        
    res = []
    if s_count == p_count:
        res.append(0)
        
    for i in range(np, ns):
        new_char = s[i]
        s_count[new_char] = s_count.get(new_char, 0) + 1
        
        old_char = s[i - np]
        s_count[old_char] -= 1
        # Logical error is kept (forgetting to delete keys when their value is 0)
        
        if s_count == p_count:
            res.append(i - np + 1)
            
    return res
