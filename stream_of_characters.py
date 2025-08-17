class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class StreamChecker:

    def __init__(self, words):
        # Build a reversed Trie of all words
        self.root = TrieNode()
        self.stream = []
        self.max_len = max(len(word) for word in words)  # optimization

        for word in words:
            node = self.root
            for ch in reversed(word):  # insert reversed word
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_word = True

    def query(self, letter: str) -> bool:
        # add new letter to the stream
        self.stream.append(letter)

        # only need last `max_len` characters
        node = self.root
        for ch in reversed(self.stream[-self.max_len:]):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_word:
                return True
        return False
