class Solution:
    def maxProfit(self, prices):

        if len(prices) < 2:
            return 0

        fst, sec, profit = 0, 0, 0
        lo, hi = prices[0], prices[0]
        val = 0

        for i in range(1, len(prices)):

            if prices[i] >= prices[i-1]:
                profit += prices[i] - prices[i-1]
            else:
                if prices[i-1] > hi:
                    hi = prices[i-1]
                    val = hi - lo

                print(f'lo={lo}, hi={hi}')

                if profit >= fst:
                    sec = fst
                    fst = profit

                elif profit < fst and profit >= sec:
                    sec = profit

                profit = 0

                print(f'fst={fst}, sec={sec}, val={val}')

        if profit >= fst:
            sec = fst
            fst = profit
        elif profit < fst and profit >= sec:
            sec = profit

        if val > sec:
            return fst + val

        return fst+sec


prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
sol = Solution()
rst = sol.maxProfit(prices)
print(rst)
