import itertools


class Solution:
    def numTilePossibilities(self, tiles):
        lst = []

        for i in range(1, len(tiles)+1):
            print([x for x in itertools.permutations(tiles, i)])
            lst.extend([x for x in itertools.permutations(tiles, i)])

        return len(set(lst))


tiles = 'AAABBC'
sol = Solution()
rst = sol.numTilePossibilities(tiles)
print(rst)
