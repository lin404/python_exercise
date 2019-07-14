class Solution:
    def kClosest(self, points, K):

        points.sort(key=lambda P: P[0]**2 + P[1]**2)
        return points[:K]


lst = [[1, 3], [-2, 2]]
k = 1
sol = Solution()
rst = sol.kClosest(lst, k)
print(rst)
