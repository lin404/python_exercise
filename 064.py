class Solution:
    def groupAnagrams(self, strs):
        tmp = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in tmp:
                tmp[key] = []
            tmp[key].append(s)

        return tmp.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
rst = Solution().groupAnagrams(strs)
print(rst)
