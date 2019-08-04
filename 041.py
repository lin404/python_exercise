class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0

        lst = [s[0]]
        num = len(lst)

        for i in range(1, len(s)):
            if s[i] in lst:
                num = max(num, len(lst))
                index = lst.index(s[i])
                lst = lst[index+1:]

            lst.append(s[i])

        num = max(num, len(lst))

        return num


s = "dvdf"
rst = Solution().lengthOfLongestSubstring(s)
print(rst)
