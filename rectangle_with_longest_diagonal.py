import math

def rectangleWithLongestDiagonal(dimensions):
    max_diagonal = -1
    max_area = -1
    
    for length, width in dimensions:
        diagonal = math.sqrt(length * length + width * width)
        area = length * width
        
        if diagonal > max_diagonal or (diagonal == max_diagonal and area > max_area):
            max_diagonal = diagonal
            max_area = area
    
    return max_area

# Example Runs
print(rectangleWithLongestDiagonal([[9,3],[8,6]]))  # Output: 48
print(rectangleWithLongestDiagonal([[3,4],[4,3]]))  # Output: 12
