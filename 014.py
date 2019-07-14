class Solution:
    def trap(self, height):
        l, r = 0, len(height)-1
        maximun, count = 0, 0

        while l < r:

            if height[l] <= height[r]:
                if height[l] < maximun:
                    count += maximun - height[l]
                else:
                    maximun = height[l]
                l += 1

            else:
                if height[r] < maximun:
                    count += maximun - height[r]
                else:
                    maximun = height[r]
                r -= 1

        return count


height = [4, 2, 3]
sol = Solution()
rst = sol.trap(height)
print(rst)
