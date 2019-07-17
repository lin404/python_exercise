class Solution:
    def minWindow(self, s, t):

        count = {}
        for char in t:

            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        cnt = len(t)
        start = 0
        minSize = 100000
        minStart = 0

        for end in range(len(s)):
            if s[end] in count:
                count[s[end]] -= 1
                if count[s[end]] >= 0:
                    cnt -= 1

            if cnt == 0:
                while True:
                    if s[start] in count:
                        if count[s[start]] < 0:
                            count[s[start]] += 1
                        else:
                            break
                    start += 1

                # print(f'start={start}, end={end}')

                if minSize > end-start+1:
                    minSize = end-start+1
                    minStart = start

        if minSize == 100000:
            return ''
        else:
            return s[minStart:minStart+minSize]


s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
rst = sol.minWindow(s, t)
print(rst)
