def find_anagrams(s: str, p: str) -> list[int]:
    ns, np = len(s), len(p)
    if np==0:
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
            left_char = s[i - np]
            s_count[left_char] -= 1

            if s_count[left_char] == 0:
                del s_count[left_char]

        if s_count == p_count:
            res.append(i - np + 1)
            
    return res
