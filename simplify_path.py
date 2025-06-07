def simplify_path(path):
    parts = path.split('/')
    stack = []

    for part in parts:
        if part == '' or part == '.':
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)

    return '/' + '/'.join(stack)

# Example usage
print(simplify_path("/home/"))  # Output: "/home"
print(simplify_path("/home//foo/"))  # Output: "/home/foo"
print(simplify_path("/../"))  # Output: "/"
print(simplify_path("/.../a/../b/c/../d/./"))  # Output: "/.../b/d"
