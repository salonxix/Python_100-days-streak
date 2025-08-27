from collections import defaultdict

MOD = 10**9 + 7

def rectangleArea(rectangles):
    # Step 1: Build events for sweep line
    events = []  # (x, type, y1, y2)
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 1, y1, y2))   # Rectangle enters
        events.append((x2, -1, y1, y2))  # Rectangle leaves

    # Step 2: Sort events by x
    events.sort()

    def calc_y_union(active):
        """Calculate total union length of y-intervals"""
        total = 0
        prev_y = -1
        count = 0
        for y1, y2 in sorted(active):
            if y1 > prev_y and count > 0:
                total += prev_y_end - prev_y
            if count == 0:
                prev_y = y1
            prev_y_end = max(prev_y if count else y1, y2)
            count += 1
            if count == 0:
                prev_y = y2
        # Recalculate properly
        merged = []
        for y1, y2 in sorted(active):
            if not merged or merged[-1][1] < y1:
                merged.append([y1, y2])
            else:
                merged[-1][1] = max(merged[-1][1], y2)
        return sum(y2 - y1 for y1, y2 in merged)

    # Step 3: Sweep line
    active = []
    prev_x = events[0][0]
    area = 0

    for x, typ, y1, y2 in events:
        # Add contribution
        area += calc_y_union(active) * (x - prev_x)
        area %= MOD

        # Update active intervals
        if typ == 1:
            active.append((y1, y2))
        else:
            active.remove((y1, y2))

        prev_x = x

    return area % MOD
