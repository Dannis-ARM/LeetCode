from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # len 0 return 0
        # On2
        # def similar(s1, s2)
        # find mathced similar for endWord matches = []

        # create a dict that tracks each words' possbile transformation lsit 
        # visited[] to track if visted
        # dfs for each every ele
        # if matched: return len(visited) wihch true

        if endWord not in wordList:
            return 0

        similar_dict = defaultdict(set)
        for word in wordList:
            for i in range(len(word)):
                word_with_start = word[:i] + "*" + word[i+1:]
                similar_dict[word_with_start].add(word)

        depth = 1
        queue = deque()
        queue.appendleft(beginWord)
        visited = set()

        while len(queue) != 0:
            queue_len = len(queue)
            for _ in range(queue_len):
                word = queue.pop()
                visited.add(word)
                if word == endWord:
                    return depth

                for i in range(len(word)):
                    word_with_start = word[:i] + "*" + word[i+1:]
                    for similar_word in similar_dict[word_with_start]:
                        if similar_word not in visited:
                            queue.appendleft(similar_word)
            depth += 1

        return 0


from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # len 0 return 0
        # On2
        # def similar(s1, s2)
        # find mathced similar for endWord matches = []

        # create a dict that tracks each words' possbile transformation lsit 
        # visited[] to track if visted
        # dfs for each every ele
        # if matched: return len(visited) wihch true

        if endWord not in wordList:
            return 0

        def similar(s1, s2):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    cnt += 1
            return cnt <= 1
        
        wordList += [beginWord]

        similar_dict = defaultdict(set)
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if similar(wordList[i], wordList[j]):
                    similar_dict[wordList[i]].add(wordList[j])
                    similar_dict[wordList[j]].add(wordList[i])
        
        depth = 1
        queue = deque()
        queue.append(beginWord)
        visited = set()

        while len(queue) != 0:
            queue_len = len(queue)
            for _ in range(queue_len):
                word = queue.popleft()
                visited.add(word)
                if word == endWord:
                    return depth

                for adjacent_word in similar_dict[word]:
                    if adjacent_word not in visited:
                        queue.append(adjacent_word)
            depth += 1
        return 0
        