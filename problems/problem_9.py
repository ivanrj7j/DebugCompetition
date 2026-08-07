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
    
    ns = len(s)
    np = len(p)

    if np == 0:
        return []
    if ns < np:
        return []

    
    p_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1

    
    s_count = {}

   
    res = []

    
    for i in range(ns):

        
        char = s[i]
        s_count[char] = s_count.get(char, 0) + 1

        
        if i >= np:

            left = s[i - np]

            s_count[left] -= 1

            
            if s_count[left] == 0:
                del s_count[left]

        
        if i >= np - 1:

            if s_count == p_count:
                res.append(i - np + 1)

    return res