from collections import defaultdict, deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        # BFS to build graph and distance map
        graph = defaultdict(list)
        distance = {beginWord: 0}
        queue = deque([beginWord])

        while queue:
            current = queue.popleft()
            for i in range(len(current)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current[:i] + c + current[i+1:]
                    if next_word in wordSet:
                        if next_word not in distance:
                            distance[next_word] = distance[current] + 1
                            queue.append(next_word)
                        if distance[next_word] == distance[current] + 1:
                            graph[current].append(next_word)

        # DFS to find all paths from beginWord to endWord
        res = []
        path = [beginWord]

        def dfs(word):
            if word == endWord:
                res.append(path[:])
                return
            for next_word in graph[word]:
                path.append(next_word)
                dfs(next_word)
                path.pop()

        dfs(beginWord)
        return res

# ---------- Example Test Case ----------
if __name__ == "__main__":
    sol = Solution()
    begin = "hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    result = sol.findLadders(begin, end, wordList)
    for seq in result:
        print(seq)
