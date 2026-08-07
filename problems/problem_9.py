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
    if ns < np or np==0:
        return []
        
    p_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1
        
    s_count = {}
    res = []
    
    # Buggy sliding window logic. The window only grows and never shrinks 
    # when the size exceeds len(p). Additionally, characters are never removed 
    # from s_count. Students must design and implement the correct sliding window 
    # map-updating bounds from scratch.
    for i in range(ns-np+1):
        s_count = {}
        for j in range(i,i+np):
            char = s[j]
            s_count[char] = s_count.get(char, 0) + 1
        
        if s_count == p_count:
            res.append(i)
            
    return res
