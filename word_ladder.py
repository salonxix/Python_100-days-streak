# ladder_length_bfs.py

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # Step 1: Create generic pattern dictionary
        L = len(beginWord)
        all_combo_dict = defaultdict(list)

        for word in wordList:
            for i in range(L):
                pattern = word[:i] + "*" + word[i+1:]
                all_combo_dict[pattern].append(word)

        # Step 2: BFS
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()

            for i in range(L):
                pattern = current_word[:i] + "*" + current_word[i+1:]

                for neighbor in all_combo_dict[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, level + 1))

                all_combo_dict[pattern] = []  # clear to reduce future lookups

        return 0


# ✅ Driver Code to Test in VS Code
if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

    sol = Solution()
    result = sol.ladderLength(begin, end, wordList)
    print("Shortest transformation sequence length:", result)
