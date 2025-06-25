# evaluate_rpn.py

class Solution:
    def evalRPN(self, tokens):
        stack = []
        
        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    # Truncate division towards zero
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]

# 🧪 Test Cases
if __name__ == "__main__":
    sol = Solution()
    print("Output 1:", sol.evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
    print("Output 2:", sol.evalRPN(["4", "13", "5", "/", "+"]))  # Output: 6
    print("Output 3:", sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # Output: 22
