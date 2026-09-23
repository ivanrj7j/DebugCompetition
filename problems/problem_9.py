def insert_interval(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    """
    You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] 
    sorted in ascending order by start_i. You are also given an interval newInterval = [start, end] 
    that represents the start and end of another interval.

    Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i 
    and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
    """
    res = []
    
    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        else:
            # Bug: Does not update newInterval[1] with max(newInterval[1], intervals[i][1])
            newInterval = [min(newInterval[0], intervals[i][0]), intervals[i][1]]
            
    res.append(newInterval)
    return res
