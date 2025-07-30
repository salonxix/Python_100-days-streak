class NestedInteger:
    def __init__(self, value=None):
        if value is None:
            self._list = []
            self._integer = None
        elif isinstance(value, int):
            self._list = None
            self._integer = value

    def isInteger(self):
        return self._integer is not None

    def add(self, elem):
        if self._list is not None:
            self._list.append(elem)
        else:
            self._list = [elem]

    def setInteger(self, value):
        self._integer = value
        self._list = None

    def getInteger(self):
        return self._integer

    def getList(self):
        return self._list

    def __repr__(self):
        if self.isInteger():
            return str(self._integer)
        return "[" + ",".join(map(str, self._list)) + "]"


def deserialize(s: str) -> NestedInteger:
    if s.isdigit() or (s[0] == '-' and s[1:].isdigit()):
        return NestedInteger(int(s))

    stack = []
    num = ''
    for ch in s:
        if ch == '[':
            stack.append(NestedInteger())
        elif ch == ']':
            if num:
                stack[-1].add(NestedInteger(int(num)))
                num = ''
            ni = stack.pop()
            if stack:
                stack[-1].add(ni)
            else:
                return ni
        elif ch == ',':
            if num:
                stack[-1].add(NestedInteger(int(num)))
                num = ''
        else:
            num += ch
    return None  # Should never reach here for valid input


# --------- Test in Terminal ---------
print("Example 1 Output:", deserialize("324"))
print("Example 2 Output:", deserialize("[123,[456,[789]]]"))
