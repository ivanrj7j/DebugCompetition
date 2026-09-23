def character_replacement(s: str, k: int) -> int:
    """
    You are given a string s and an integer k. You can choose any character of the string 
    and change it to any other uppercase English character. You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.
    """
    count = {}
    res = 0
    l = 0
    maxf = 0
    
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        maxf = max(maxf, count[s[r]])
        
        # Bug: Indentation error putting res calculation inside the shrink loop
        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
            res = max(res, r - l + 1)
            
    return res
