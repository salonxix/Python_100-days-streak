def pushDominoes(dominoes: str) -> str:
    """
    Determine the final state of dominoes after they finish falling.
    
    Args:
        dominoes: String representing initial state ('L', 'R', or '.')
        
    Returns:
        String representing the final state after all dominoes fall
    """
    n = len(dominoes)
    forces = [0] * n
    
    # Calculate rightward forces
    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n
        elif dominoes[i] == 'L':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] += force
    
    # Calculate leftward forces
    force = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            force = n
        elif dominoes[i] == 'R':
            force = 0
        else:
            force = max(force - 1, 0)
        forces[i] -= force
    
    # Determine final state based on net forces
    result = []
    for f in forces:
        if f > 0:
            result.append('R')
        elif f < 0:
            result.append('L')
        else:
            result.append('.')
    
    return ''.join(result)

# Test cases
def test_solution():
    # Example 1
    dominoes1 = "RR.L"
    print(f"Input: {dominoes1}")
    print(f"Output: {pushDominoes(dominoes1)}")  # Expected: "RR.L"
    print()
    
    # Example 2
    dominoes2 = ".L.R...LR..L.."
    print(f"Input: {dominoes2}")
    print(f"Output: {pushDominoes(dominoes2)}")  # Expected: "LL.RR.LLRRLL.."
    print()

if __name__ == "__main__":
    test_solution()
