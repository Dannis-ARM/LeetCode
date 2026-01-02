from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # becuase nums1 is nums2's subset
        # we can try get each value for nums2
        # back for loop nums2
        # if cur val < stack[-1]
        # res.insert(0, cur_val)
        # stack.append(cur_val)
        # else:
        # stack keep pop until it meet condition / and let res.insert / if empty stil fail res.insert[0, 0-1]
        # stack.append(cur_val)
        # return res
        
        res = {}
        stack = [] # bigger elements # mono bigger elemetns
        for num in nums2[::-1]:
            if len(stack) == 0:
                res[num] = -1
                stack.append(num)
                continue
            
            if num < stack[-1]:
                res[num] = stack[-1]
                stack.append(num)
            else:
                while len(stack) != 0 and num > stack[-1]:
                    stack.pop()
                
                if len(stack) == 0:
                    res[num] = -1
                    stack.append(num)
                else:
                    res[num] = stack[-1]
                    stack.append(num)
        
        return [res[num] for num in nums1]
            


from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # becuase nums1 is nums2's subset
        # we can try get each value for nums2
        # back for loop nums2
        # if cur val < stack[-1]
        # res.insert(0, cur_val)
        # stack.append(cur_val)
        # else:
        # stack keep pop until it meet condition / and let res.insert / if empty stil fail res.insert[0, 0-1]
        # stack.append(cur_val)
        # return res
        
        res = {}
        stack = [] # bigger elements # mono bigger elemetns
        for num in nums2[::-1]:
            if len(stack) == 0:
                res[num] = -1
                stack.append(num)
                continue
            
            while len(stack) != 0 and num > stack[-1]:
                stack.pop()

            if len(stack) == 0:
                res[num] = -1
            else:
                res[num] = stack[-1]
            stack.append(num)
        
        return [res[num] for num in nums1]
            

        