class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = next(iterator, None)  # store the first element in advance

    def peek(self):
        return self._next  # just return without moving

    def next(self):
        current = self._next
        self._next = next(self.iterator, None)  # move pointer to next element
        return current

    def hasNext(self):
        return self._next is not None


# Example usage:
nums = iter([1, 2, 3])
peekingIterator = PeekingIterator(nums)

print(peekingIterator.next())    # 1
print(peekingIterator.peek())    # 2
print(peekingIterator.next())    # 2
print(peekingIterator.next())    # 3
print(peekingIterator.hasNext()) # False
