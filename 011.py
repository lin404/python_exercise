class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ''
        for i in range(0, len(s)):

            odd = self.helper(s, i, i)
            even = self.helper(s, i, i+1)
            longest = max(longest, odd, even, key=len)

        return longest

    def helper(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1

        return s[i+1:j]


s = 'abb'
sol = Solution()
rst = sol.longestPalindrome(s)
print(rst)
