class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack: all elemetns has to be greater cur arr[i]
        # back for loop arr
        # if arr[i] < stack[-1]:
        # res[i] = popi - i
        # else
        # stack pop()
        # append cur arr[i] into stack

        res = [0 for _ in range(len(temperatures))]
        stack = []
        for i in range(len(temperatures)-1, -1, -1):
            while len(stack) != 0:
                if temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                else:
                    res[i] = stack[-1] - i
                    break
            stack.append(i)
        return res