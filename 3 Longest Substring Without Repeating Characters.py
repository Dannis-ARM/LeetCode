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
