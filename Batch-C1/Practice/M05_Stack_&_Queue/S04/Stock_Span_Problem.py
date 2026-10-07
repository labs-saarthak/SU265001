class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_price,prev_span = self.stack.pop()
            span += prev_span
        self.stack.append((price,span))
        return span

#Input
in1 = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
in2 = [[], [100], [80], [60], [70], [60], [75], [85]]
output = []
obj = None
for method,val in zip(in1,in2):
    if method == "StockSpanner":
        obj = StockSpanner()
        output.append(None)
    elif method == "next":
        output.append(obj.next(val[0]))
print(output)
    
