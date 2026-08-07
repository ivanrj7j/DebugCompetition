import collections
def group_anagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = collections.defaultdict(list)
    
    for s in strs:
        key = tuple(sorted(s))
        anagram_map[key].append(s)
        
    return list(anagram_map.values())
