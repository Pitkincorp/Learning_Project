def sum_of_intervals(intervals):
    i = 0
    while i in range(len(intervals)):
        for j in range(i+1,len(intervals)):
            if intervals[j][0] <= intervals[i][0] <= intervals[j][1]:
                intervals[i] = (intervals[j][0],intervals[i][1])
                if intervals[i][1] < intervals[j][1]:
                    intervals[i] = (intervals[i][0],intervals[j][1])
                del intervals[j]
                break
            if intervals[i][0] <= intervals[j][0] <= intervals[i][1]:
                if intervals[i][1] < intervals[j][1]:
                    intervals[i] = (intervals[i][0],intervals[j][1])
                del intervals[j]
                break
        else: i += 1
    return sum([i[1]-i[0] for i in intervals])


print(sum_of_intervals([(2, 5), (-7, 5),(4, 9), (13,16)]))