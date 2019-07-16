import collections
import operator
import heapq


class Solution:

    def topKFrequentSimpler(self, words, k):
        # count is like map
        count = collections.Counter(words)

        # count.items() is like tuple
        # heap is the list of tuples
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        print(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]

    def topKFrequentSort(self, words, k):
        # count is like map
        count = collections.Counter(words)
        candidates = sorted(count.keys(), key=lambda w: (-count[w], w))
        print(candidates)
        return candidates[:k]

    def topKFrequent(self, words, k):

        dic = collections.OrderedDict()
        lst = []

        for w in words:
            if w in dic:
                dic[w] += 1
            else:
                dic[w] = 1

        d = collections.OrderedDict(
            sorted(dic.items(), key=operator.itemgetter(1)))

        # print(d)
        maximum = 0
        pre = []
        for _ in range(len(dic)):
            tup = d.popitem()
            if tup[1] >= maximum:
                pre.append(tup[0])
                pre.sort()
            else:
                lst.extend(pre)
                pre = []
                pre.append(tup[0])

            maximum = tup[1]

        lst.extend(pre)
        return lst[:k]


words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 3

sol = Solution()
rst = sol.topKFrequentSort(words, k)
print(rst)
