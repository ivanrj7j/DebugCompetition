def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Given an array of intervals where intervals[i] = [start_i, end_i], merge all 
    overlapping intervals, and return an array of the non-overlapping intervals 
    that cover all the intervals in the input.

    Examples:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
    """
    if not intervals:
        return []

    sorted_intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
    merged = [sorted_intervals[0]]

    for start, end in sorted_intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1][1] = max(last_end, end)
        else:
            merged.append([start, end])

    return merged
