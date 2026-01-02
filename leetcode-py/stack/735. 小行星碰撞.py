class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack - all survived asteroids
        
        # for survived nodes
        # check last surviced
        # if same dir as left side: just append
        # not same dir
        # if same value: smash together
        # if left bigger: keep pop to smash until if poped same dir or larger
        # if cur samller: gone

        stack = []
        for a in asteroids:
            if len(stack) == 0 or a > 0:
                stack.append(a)
            else:
                while len(stack) != 0:
                    abs_a = -a
                    if stack[-1] < 0:
                        stack.append(a)
                        break
                    elif abs_a == stack[-1]:
                        stack.pop()
                        break
                    elif stack[-1] > abs_a:
                        break
                    else: # stack[-1] < abs_a
                        stack.pop()
                        if len(stack) == 0:
                            stack.append(a)
                            break
        return stack
    
### better
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        小行星碰撞问题：
        - 栈存储存活的小行星
        - 碰撞条件：栈顶小行星向右（正数），当前小行星向左（负数）
        - 碰撞规则：绝对值大的存活，相等则都销毁，小的则被销毁
        """
        stack = []
        for curr in asteroids:
            # 标记当前小行星是否存活（是否需要入栈）
            alive = True
            # 只有当当前小行星向左，且栈顶向右时，才会发生碰撞
            while alive and curr < 0 and stack and stack[-1] > 0:
                # 计算当前向左小行星的绝对值（大小）
                curr_size = -curr
                top_size = stack[-1]
                if curr_size == top_size:
                    # 两者大小相等，都销毁
                    stack.pop()
                    alive = False
                elif curr_size > top_size:
                    # 栈顶小行星被撞毁，继续检查下一个栈顶
                    stack.pop()
                else:
                    # 当前小行星被撞毁
                    alive = False
            # 如果当前小行星存活，入栈
            if alive:
                stack.append(curr)
        return stack