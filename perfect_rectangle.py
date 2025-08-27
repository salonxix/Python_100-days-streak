def isRectangleCover(rectangles):
    corner_set = set()
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')
    area_sum = 0

    for x1, y1, x2, y2 in rectangles:
        # Update bounding rectangle
        min_x = min(min_x, x1)
        min_y = min(min_y, y1)
        max_x = max(max_x, x2)
        max_y = max(max_y, y2)

        # Add area
        area_sum += (x2 - x1) * (y2 - y1)

        # Define 4 corners of each rectangle
        corners = [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]

        # Toggle corner presence in set
        for c in corners:
            if c in corner_set:
                corner_set.remove(c)
            else:
                corner_set.add(c)

    # Expected final corners
    expected_corners = {(min_x, min_y), (min_x, max_y), 
                        (max_x, min_y), (max_x, max_y)}

    # Bounding rectangle area
    bounding_area = (max_x - min_x) * (max_y - min_y)

    # Final check
    return area_sum == bounding_area and corner_set == expected_corners
