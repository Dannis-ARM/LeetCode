# 给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。

# 注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

# 示例 1：

# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
# 示例 2：

# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
#      注意，你可以重复使用字典中的单词。
# 示例 3：

# 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false

# brute force
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def can_break(s: str):
            if s == "":
                return True
            if s in wordDict:
                return True
            
            can = False
            for word in wordDict:
                r = len(word)
                if len(s) < r:
                    continue
                if s[:r] == word:
                    if can_break(s[r:]) is True:
                        can = True
                        break
            return can

        return can_break(s)                

# search + memo
# brute force
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}
        def can_break(s: str):
            if s in memo:
                return memo[s]
            if s == "":
                return True
            if s in wordDict:
                return True
            
            can = False
            for word in wordDict:
                r = len(word)
                if len(s) < r:
                    continue
                if s[:r] != word:
                    continue
                
                memo[s[r:]] = can_break(s[r:])
                if memo[s[r:]] is True:
                    return True
            return can

        return can_break(s)                
        