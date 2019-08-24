class Solution:
    def generateParenthesis(self, n):
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + '(')
            print(f'left={path}')
        if left < right:
            self.dfs(res, left, right - 1, path + ')')
            print(f'right={path}')


n = 3
rst = Solution().generateParenthesis(n)
print(rst)
