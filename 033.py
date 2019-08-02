
class Solution:
    def calcEquation(self, equations, values, queries):

        var_map = {}

        for idx, strs in enumerate(equations):

            if strs[0] not in var_map:
                var_map[strs[0]] = {}

            if strs[1] not in var_map:
                var_map[strs[1]] = {}

            var_map[strs[0]][strs[1]] = values[idx]
            var_map[strs[1]][strs[0]] = 1/values[idx]

        lst = []

        for var in queries:
            if var[0] not in var_map or var[1] not in var_map:
                lst.append(float(-1))

            elif var[0] == var[1] and var[0] in var_map:
                lst.append(float(1))

            else:
                if var[1] in var_map[var[0]]:
                    lst.append(float(var_map[var[0]][var[1]]))
                elif var[0] in var_map[var[1]]:
                    lst.append(float(var_map[var[0]][var[1]]))
                else:
                    for key, value in var_map[var[0]].items():
                        if key in var_map[var[1]]:
                            lst.append(float(value/var_map[var[1]][key]))
        return lst


equations = [["a", "b"]]
values = [0.5]
queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]

sol = Solution()
rst = sol.calcEquation(equations, values, queries)
print(rst)
