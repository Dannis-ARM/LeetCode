class Solution:
    def isValid(self, s: str) -> bool:
        dct = {}
        dct['('] = ')'
        dct['{'] = '}'
        dct['['] = ']'

        stack = []

        for c in s:
            if c in dct.keys():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                k = stack.pop()
                if dct[k] != c:
                    return False
        return len(stack) == 0        