class StockSpanner:

    def __init__(self):
        self.stack = []  # stores pairs [price, span]

    def next(self, price: int) -> int:
        span = 1
        # pop all smaller or equal prices and add their spans
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span])
        return span
