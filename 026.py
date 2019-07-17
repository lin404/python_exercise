class Solution:
    def licenseKeyFormatting(self, S, K):
        res = []
        s = "".join(S.split("-")).upper()

        N = len(s)
        if N % K != 0:
            res.append(s[: N % K])

        for i in range(N % K, N, K):
            res.append(s[i: i + K])

        return "-".join(res)


S = "5F3Z-2e-9-w"
K = 4
sol = Solution()
rst = sol.licenseKeyFormatting(S, K)
print(rst)
