# 给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

# 一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

# 例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
# 两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # i j out of bounds, return 0
        # if (t[i]==t[j])
        # longest i,j  is longest(i-1,j-1) + 1
        # else
        # its max(longest(i-1,j), longest(i, j-1))

        memo = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def longest(i, j):
            if i < 0 or j <0 or i >= len(text1) or j >= len(text2):
                return 0
            if memo[i][j] != -1:
                return memo[i][j]

            if text1[i] == text2[j]:
                memo[i][j] = longest(i-1, j-1) + 1
            else:
                memo[i][j] = max(longest(i-1, j), longest(i, j-1))

            return memo[i][j]
        
        return longest(len(text1)-1, len(text2)-1)