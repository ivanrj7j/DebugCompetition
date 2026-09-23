def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    """
    Given an array of intervals intervals where intervals[i] = [start_i, end_i], 
    return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
    """
    if not intervals:
        return 0
        
    intervals.sort(key=lambda x: x[0])  # Bug: Sorting by start time instead of end time (x[1])
    
    count = 0
    prev_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < prev_end:
            count += 1
            prev_end = min(prev_end, intervals[i][1])
        else:
            prev_end = intervals[i][1]
            
    return count
