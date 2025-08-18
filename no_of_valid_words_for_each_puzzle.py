from collections import Counter

class Solution:
    def findNumOfValidWords(self, words, puzzles):
        # Convert word -> bitmask
        def get_mask(word):
            mask = 0
            for ch in set(word):  # use set to avoid duplicate letters
                mask |= 1 << (ord(ch) - ord('a'))
            return mask

        # Step 1: Store word frequencies by bitmask
        word_count = Counter(get_mask(w) for w in words)

        ans = []
        # Step 2: Process each puzzle
        for puzzle in puzzles:
            first_char_mask = 1 << (ord(puzzle[0]) - ord('a'))
            puzzle_mask = get_mask(puzzle)

            # Generate subsets of puzzle letters
            submask = puzzle_mask
            total = 0
            while submask:
                # Check if subset contains first char
                if submask & first_char_mask:
                    total += word_count[submask]
                submask = (submask - 1) & puzzle_mask  # move to next subset

            ans.append(total)

        return ans
