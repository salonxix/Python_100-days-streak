def camelMatch(queries, pattern):
    def matches(query, pattern):
        i, j = 0, 0
        while i < len(query):
            if j < len(pattern) and query[i] == pattern[j]:
                j += 1  # match pattern character
            elif query[i].isupper():
                return False  # extra uppercase not allowed
            i += 1
        return j == len(pattern)

    return [matches(query, pattern) for query in queries]


# Example test cases
queries1 = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern1 = "FB"
print(camelMatch(queries1, pattern1))  # [True, False, True, True, False]

queries2 = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern2 = "FoBa"
print(camelMatch(queries2, pattern2))  # [True, False, True, False, False]

queries3 = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
pattern3 = "FoBaT"
print(camelMatch(queries3, pattern3))  # [False, True, False, False, False]
