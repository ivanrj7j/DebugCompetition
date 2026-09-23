import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Given an integer array nums and an integer k, return the k most frequent elements.
    You may return the answer in any order.
    """
    count = Counter(nums)
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
            
    res = []
    while heap:
        res.append(heapq.heappop(heap)[0])  # Bug: appends frequency instead of num (index 0 instead of index 1)
        
    return res
