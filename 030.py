class Solution:
    def merge(self, intervals):

        intervals = sorted(intervals, key=lambda k: k[0])
        l = 1
        while l < len(intervals):
            pre = intervals[l-1]
            cur = intervals[l]
            if pre[0] <= cur[0] <= pre[1]:
                intervals[l][0] = intervals[l-1][0]
                intervals[l][1] = max(intervals[l-1][1], intervals[l][1])
                del intervals[l-1]
            else:
                l += 1

        return intervals


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
sol = Solution()
rst = sol.merge(intervals)
print(rst)
