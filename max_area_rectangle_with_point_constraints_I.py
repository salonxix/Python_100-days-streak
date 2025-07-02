def maxAreaRect(points):
    point_set = set(map(tuple, points))
    max_area = -1

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Skip if not diagonal
            if x1 == x2 or y1 == y2:
                continue

            # Check if the other two corners exist
            if (x1, y2) in point_set and (x2, y1) in point_set:
                # Check for any point inside the rectangle
                valid = True
                for x, y in point_set:
                    if min(x1, x2) < x < max(x1, x2) and min(y1, y2) < y < max(y1, y2):
                        valid = False
                        break
                if valid:
                    area = abs(x2 - x1) * abs(y2 - y1)
                    max_area = max(max_area, area)

    return max_area

# ------------ INPUT & OUTPUT ------------
if __name__ == "__main__":
    # You can modify this input for custom testing
    points = [[1,1],[1,3],[3,1],[3,3],[1,2],[3,2]]
    result = maxAreaRect(points)
    print("Maximum Area Rectangle (with constraints):", result)
