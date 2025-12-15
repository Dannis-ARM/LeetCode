# bruteforce
class Solution:
    def removeDuplicates(self, s: str) -> str:
        pre_cur = cur = len(s)

        while True:
            for i in range(1, len(s)):
                if s[i] == s[i-1]:
                    s = s[:i-1] + s[i+1:]
                    break
            cur = len(s)
            if cur == pre_cur:
                break
            pre_cur = cur
        return s


### pass
class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)

        if len(s) == 2:
            if s[0] == s[1]:
                return ""
            else:
                return "".join(s)
        
        if len(s) < 2:
            return "".join(s)
        
        i, j = 0, 1
        while True:
            if j >= len(s):
                break
            i += 1
            s[i] = s[j]
            if i >= 1 and s[i] == s[i-1]:
                i = i - 2
            j += 1
        return "".join(s[:i+1])

### clear

class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) < 2:
            return s
        
        s = list(s)
        i = 0

        for j in range(1, len(s)):
            i += 1
            s[i] = s[j]
            if i >= 1 and s[i] == s[i-1]:
                i = i - 2
        return "".join(s[:i+1])
