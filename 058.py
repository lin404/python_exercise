class Solution:
    def decodeString(self, s):

        curnum = 0
        curstring = ''
        stack = []
        for v in s:
            if v == '[':
                stack.append(curnum)
                stack.append(curstring)
                curnum = 0
                curstring = ''
            elif v == ']':
                prestring = stack.pop()
                prenum = stack.pop()
                curstring = prestring + prenum * curstring
            elif v.isdigit():
                curnum = curnum * 10 + int(v)
            else:
                curstring += v

        return curstring


s = "3[a2[b]]"
rst = Solution().decodeString(s)
print(rst)
