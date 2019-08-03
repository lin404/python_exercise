import collections


class Solution:
    def findJudge(self, N, trust):

        p = {i: {} for i in range(1, N+1)}
        for (x, y) in trust:
            p[x][y] = 1

        for key, value in p.items():
            if len(value) == 0:
                j = key
                for k, v in p.items():
                    if k != j and j not in v:
                        return -1
                return j
        return -1


N = 2
trust = [[2, 1]]
rst = Solution().findJudge(N, trust)
print(rst)
