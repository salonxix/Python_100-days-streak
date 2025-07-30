class NestedInteger:
    # If value is an integer, we store it directly
    # If value is a list, we convert each element to a NestedInteger
    def __init__(self, value):
        if isinstance(value, int):
            self._integer = value
            self._list = None
        else:
            self._integer = None
            self._list = [NestedInteger(x) for x in value]

    def isInteger(self):
        return self._integer is not None

    def getInteger(self):
        return self._integer

    def getList(self):
        return self._list


class NestedIterator:
    def __init__(self, nestedList):
        # Stack of NestedInteger elements (reversed for LIFO order)
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop().getInteger()

    def hasNext(self):
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(top.getList()[::-1])
        return False


# --- MAIN SECTION FOR TERMINAL OUTPUT ---

# Example 1: nestedList = [[1,1],2,[1,1]]
nested_input = NestedInteger([[1,1]])
nested_input2 = NestedInteger(2)
nested_input3 = NestedInteger([1,1])
nestedList = [nested_input, nested_input2, nested_input3]

# Initialize iterator
iterator = NestedIterator(nestedList)

# Collect result
res = []
while iterator.hasNext():
    res.append(iterator.next())

# Print the output to terminal
print("Flattened list:", res)
