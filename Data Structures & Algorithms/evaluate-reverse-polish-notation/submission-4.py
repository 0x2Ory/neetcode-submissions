class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for c in tokens:
            if c == "+":
                x = res.pop()
                y = res.pop()
                z = x + y
                res.append(z)
            elif c == "-":
                z = res.pop() - res.pop()
                res.append(z)
            elif c == "*":
                res.append(res.pop() * res.pop())
            elif c == "/":
                res.append(int(res.pop()) / int(res.pop()))
            else:
                res.append(int(c))
        return res[0]