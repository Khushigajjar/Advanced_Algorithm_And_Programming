def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0]) 
    merged = []
    current = intervals[0]

    for i in range(1, len(intervals)):
        next_interval = intervals[i]
        if next_interval[0] <= current[1]: 
            current[1] = max(current[1], next_interval[1])
        else:
            merged.append(current)
            current = next_interval
    merged.append(current)
    return merged

print(merge_intervals([[1,3], [2,6], [8,10], [15,18]]))