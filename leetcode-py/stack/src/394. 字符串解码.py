class Solution:
    def decodeString(self, s: str) -> str:
        # stack
        # acceept left [
        # once meet ] pop left [ to get idx -> also can get k
        # then from right to left, insert into s at ]

        stack = list()
        for char in s:
            if char.isdigit() or char == '[' or char.isalpha():
                stack.append(char)
            elif char == ']':
                fetch_s = []
                while stack[-1] != '[':
                    char = stack.pop()
                    fetch_s.append(char)
                stack.pop() # get rid of [
                fetch_s.reverse()
                fetch_s = "".join(fetch_s)

                cnt = list()
                while len(stack) >0 and stack[-1].isdigit():
                    cnt.append(stack.pop())
                cnt.reverse()
                cnt = int("".join(cnt))
                
                concat_fetch_s = "".join([fetch_s for _ in range(cnt)])
                stack.append(concat_fetch_s)
            else:
                assert False
        return "".join(stack)
            