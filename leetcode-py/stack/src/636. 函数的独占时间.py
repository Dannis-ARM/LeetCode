class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # function stack - 
        # for loop time

        # prev_time = 0
        # if met start ->
        # # top peek get running time = cur - prev_time
        # # push new met start 
        # # prev_time = cur
        # # dct[peek_item] += running time
        # if met end ->
        # # pop top and  get this func call's running time = cur - prev_time + 1
        # set dct[function call] += running time

        prev_time = 0
        stack = []

        res = [0 for _ in range(n)]
        for log in logs:
            _id, state, cur = log.split(":")
            
            cur = int(cur)
            _id = int(_id)
            log = [_id, state, cur] 

            if state == 'start':
                if len(stack) == 0:
                    stack.append(log)
                    prev_time = cur
                    continue

                top_id = stack[-1][0]
                res[top_id] += cur - prev_time                    
                prev_time = cur
                stack.append(log)
            else:
                stack.pop()
                res[_id] += cur - prev_time + 1                   
                prev_time = cur + 1
        return res

