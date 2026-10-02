class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort(key = lambda x : x[1])

        keep = 0

        curEnd = float('-INF')
        for s, e in intervals:
            if s >= curEnd:
                keep+=1
                curEnd = e
        
        return len(intervals) - keep