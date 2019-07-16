class Solution:
    def gardenNoAdj(self, N, paths):

        res = [0] * N
        graph = [[] for i in range(N)]

        for p in paths:
            graph[p[0]-1].append(p[1]-1)
            graph[p[1]-1].append(p[0]-1)

        for i in range(N):
            colorLst = []
            for num in graph[i]:
                colorLst.append(res[num])

            for color in range(1, 5):
                if color not in colorLst:
                    res[i] = color
                    break

        return res


N = 6
paths = [[6, 4], [6, 1], [3, 1], [4, 5], [2, 1], [5, 6], [5, 2]]
sol = Solution()
rst = sol.gardenNoAdj(N, paths)
print(rst)
