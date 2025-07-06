from itertools import combinations

def find_max_triangle_area(coords):
    max_area2 = 0  # store 2 * area to avoid floating point
    n = len(coords)

    for a, b, c in combinations(coords, 3):
        x1, y1 = a
        x2, y2 = b
        x3, y3 = c

        # Shoelace formula for 2*Area
        area2 = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))

        if area2 == 0:
            continue  # ignore degenerate triangles

        # Check if any side is horizontal or vertical
        if (x1 == x2 or y1 == y2) or (x2 == x3 or y2 == y3) or (x1 == x3 or y1 == y3):
            max_area2 = max(max_area2, area2)

    return max_area2 if max_area2 > 0 else -1

# 🔍 Test Cases
coords1 = [[1,1],[1,2],[3,2],[3,3]]
print(find_max_triangle_area(coords1))  # Output: 2

coords2 = [[1,1],[2,2],[3,3]]
print(find_max_triangle_area(coords2))  # Output: -1
