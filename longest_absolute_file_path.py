def lengthLongestPath(input_str):
    max_length = 0
    path_length = {0: 0}  # depth : total path length up to this depth

    for line in input_str.split('\n'):
        name = line.lstrip('\t')
        depth = len(line) - len(name)

        if '.' in name:  # It's a file
            max_length = max(max_length, path_length[depth] + len(name))
        else:  # It's a directory
            path_length[depth + 1] = path_length[depth] + len(name) + 1  # add '/' as well

    return max_length

# Terminal interaction
input_str = input("Enter the file system string:\n")
result = lengthLongestPath(input_str)
print("Longest absolute path length:", result)
