import sys


class Solution:

    # O(n)
    def maximumProductFaster(self, nums):
        if len(nums) < 3:
            return -1

        min1 = min2 = sys.maxsize
        max1 = max2 = max3 = -sys.maxsize

        for num in nums:

            if num >= max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2:
                max3 = max2
                max2 = num
            elif num >= max3:
                max3 = num

            if num <= min1:
                min2 = min1
                min1 = num
            elif num <= min2:
                min2 = num

        return max(min1*min2*max1, max1*max2*max3)

    # sorted -> O(nlogn)

    def maximumProduct(self, nums):
        if len(nums) < 3:
            return -1

        nums.sort()

        return max(nums[0]*nums[1]*nums[-1], nums[-1]*nums[-2]*nums[-3])


nums = [-7, -3, -1, 0]
sol = Solution()
rst = sol.maximumProductFaster(nums)
print(rst)
