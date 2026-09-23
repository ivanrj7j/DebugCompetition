def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    Given an array of integers temperatures represents the daily temperatures, return an array answer 
    such that answer[i] is the number of days you have to wait after the i-th day to get a warmer temperature. 
    If there is no future day for which this is possible, keep answer[i] == 0 instead.
    """
    res = [0] * len(temperatures)
    stack = []  # will store indices
    
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            prev_i = stack.pop()
            res[prev_i] = i  # Bug: stores absolute index i instead of relative days (i - prev_i)
        stack.append(i)
        
    return res
