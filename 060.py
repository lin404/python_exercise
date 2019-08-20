class Solution:
    def search(self, nums, target):

        left, right = 0, len(nums)-1

        while left <= right:
            mid = int((left+right)/2)
            print(f'mid={mid}')
            if nums[mid] == target:
                return mid

            elif nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

            print(f'left={left}, right={right}')

        return -1


nums = [3, 1]
target = 1
rst = Solution().search(nums, target)
print(rst)
