class Solution:
    def productExceptSelf(self, nums):

        p = 1
        n = len(nums)
        answer = [1]*n

        for i in range(n):
            answer[i] *= p
            p *= nums[i]

        print(answer)

        p = 1
        # for i in range(n-1, -1, -1):
        for i in reversed(range(n)):
            answer[i] *= p
            p *= nums[i]

        return answer


nums = [1, 2, 3, 4]
sol = Solution()
rst = sol.productExceptSelf(nums)
print(rst)
