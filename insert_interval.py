class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        #keeps track of the input point
        cnt = 0
        
        #add intervals that don't overlap
        for x,y in intervals:
            if newInterval[0] > y:
                res.append([x,y])
                cnt += 1
            else:
                break

        #merge interval or append newInterval if everything is added
        if cnt < len(intervals) and intervals[cnt][1] >= newInterval[0] >= intervals[cnt][0]:
            m = min(newInterval[0], intervals[cnt][0])
            n = max(newInterval[1], intervals[cnt][1])
            res.append([m,n])
        else:
            res.append(newInterval)
        
        #the last item in res is the updated newInterval
        if cnt < len(intervals):
            for i in range(cnt, len(intervals)):
                if intervals[i][0] > res[-1][1]:
                    res = res + intervals[i:]
                    return res
                else:
                    res[-1][0] = min(res[-1][0], intervals[i][0])
                    res[-1][1] = max(res[-1][1], intervals[i][1])

        return res