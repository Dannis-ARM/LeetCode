### 3
解决方案：滑动窗口 (Sliding Window)解决这个问题最有效的方法是使用 滑动窗口 (Sliding Window) 算法。核心思想维护一个 窗口 (通常由两个指针 $i$ 和 $j$ 定义，分别代表窗口的起始和结束位置)，这个窗口内的子串必须是 无重复字符 的。在遍历字符串时，不断向右移动窗口的结束指针 $j$，扩大窗口。每次扩大窗口后，检查新加入的字符是否已经在当前窗口中出现过。如果 没有重复，说明窗口仍然有效，我们更新迄今为止找到的最长子串长度，然后继续向右移动 $j$。如果 出现重复，说明当前窗口不再有效，必须缩小窗口。我们将窗口的起始指针 $i$ 向右移动，直到重复的字符被移除，使窗口重新变得有效 (即窗口内无重复字符)。为了高效地检查字符是否重复以及快速定位重复字符的位置，我们可以使用一个 哈希集合 (HashSet) 或 哈希表/字典 (HashMap/Dictionary) 来存储窗口内的字符及其位置。使用 HashMap 优化移动 $i$ 的步骤使用 哈希表 (Map) 来存储窗口内字符和它们在字符串中的 索引位置，可以进一步优化算法。Map 存储：$key$ 是字符， $value$ 是它在字符串 $s$ 中的索引。当 $j$ 向右移动，遇到重复字符 $s[j]$ 时：假设 $s[j]$ 上一次出现在索引 $k$ (即 $map[s[j]] = k$)。我们不需要 $i$ 一步一步地移动，可以直接将窗口起始指针 $i$ 移动到 $k+1$ 的位置。但是，需要注意的是 $i$ 只能向前移动，不能后退。因此，新的 $i$ 应该是 $\max(i, map[s[j]] + 1)$。无论是否重复，我们都更新 $s[j]$ 在 Map 中的索引为当前的 $j$。最长长度：在每次移动 $j$ 后，新的窗口长度为 $j - i + 1$，我们用它来更新最大长度 $\max\_len = \max(\max\_len, j - i + 1)$。


# Bruteforce O(n**2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (str == None or len(s) == 0):
            return 0
        counts = []
        for i in range(len(s)):
            count = 1
            prevMap = {}
            prevMap[s[i]] = i
            for j in range(i+1, len(s)):
                if s[j] in prevMap:
                    break
                count += 1
                prevMap[s[j]] = j

            counts.append(count)
        return max(counts)

# Sliding Window O(n)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (str == None or len(s) == 0):
            return 0
        m = n = 0
        maxCount = count = 1
        length = len(s)
        prevMap = {}
        prevMap[s[m]] = 1
        while(True):
            while(n < length-1):
                n += 1
                count += 1
                if (s[n] in prevMap):
                    break
                maxCount = max(maxCount, count)
                prevMap[s[n]] = 1

            while(m < n and s[n] in prevMap):
                if (s[n] != s[m]):
                    del prevMap[s[m]]
                    m += 1
                    count -= 1
                else:
                    m += 1
                    count -= 1
                    break
            if (n == length-1):
                break
        return maxCount


# Neet Code O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = maxCount = count = 0
        mp = {}
        while(right <= len(s)-1):
            if (s[right] in mp and left <= mp[s[right]]):
                count = right - mp[s[right]]
                left = mp[s[right]]+1
            else:
                count += 1
                maxCount = max(maxCount, count)
            mp[s[right]] = right
            right += 1
        return maxCount


if __name__ == "__main__":
    s = Solution()
    res = s.lengthOfLongestSubstring("tmmzuxt")
    print(res)
