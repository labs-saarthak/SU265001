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
res = []
obj = None
for x,y in zip(in1,in2):
    if x == "StockSpanner":
        obj = StockSpanner()
        res.append(None)
    elif x == "next":
        res.append(obj.next(y[0]))
print(res)