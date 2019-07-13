import sys


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        lst1, lst2 = sorted((nums1, nums2), key=len)
        x, y = len(lst1), len(lst2)
        lo, hi = 0, x

        # [],[1]
        while lo <= hi:
            xpartition = (lo + hi + 1)//2
            ypartition = (x + y + 1)//2 - xpartition

            print(f'xpartition={xpartition}, y={ypartition}')

            xleft = lst1[xpartition-1] if xpartition > 0 else -sys.maxsize
            xright = lst1[xpartition] if xpartition < x else sys.maxsize

            yleft = lst2[ypartition-1] if ypartition > 0 else -sys.maxsize
            yright = lst2[ypartition] if ypartition < y else sys.maxsize

            print(
                f'xleft={xleft}, xright={xright}, yleft={yleft}, yright={yright}')

            # [1],[1]
            if xleft <= yright and yleft <= xright:
                if (x+y) % 2 == 0:
                    return (max(xleft, yleft)+min(xright, yright))/2
                else:
                    return max(xleft, yleft)

            if xleft > yright:
                hi = xpartition - 1

            elif yleft > xright:
                lo = xpartition + 1


nums1, nums2 = [1], [1]
sol = Solution()
rst = sol.findMedianSortedArrays(nums1, nums2)
print(rst)
