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
    if np == 0 or ns < np:
        return []
        
    p_count = {}
    for char in p:
        p_count[char] = p_count.get(char, 0) + 1
        
    s_count = {}
    res = []
    left = 0
    
    for right in range(ns):
        char = s[right]
        s_count[char] = s_count.get(char, 0) + 1

        # Shrink window if size exceeds p length
        if right - left + 1 > np:
            left_char = s[left]
            s_count[left_char] -= 1

            if s_count[left_char] == 0:
                del s_count[left_char]

            left += 1

        # Check if current window is an anagram
        if s_count == p_count:
            res.append(left)
            
    return res
