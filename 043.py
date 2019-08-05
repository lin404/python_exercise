import collections
import heapq


class Solution:
    def topKFrequent_Heap(self, nums, k):
        count = collections.Counter(nums)
        return heapq.nlargest(k, count.keys(), key=lambda k: count[k])

    def topKFrequent_List(self, nums, k):

        count = collections.Counter(nums)
        return sorted(count.keys(), key=count.get, reverse=True)[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
ans = Solution().topKFrequent_List(nums, k)
print(ans)
ans = Solution().topKFrequent_Heap(nums, k)
print(ans)
