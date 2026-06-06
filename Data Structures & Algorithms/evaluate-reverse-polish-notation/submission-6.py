class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for c in tokens:
            if c == "+":
                res.append(res.pop()+ res.pop())
            elif c == "-":
                x = res.pop()
                y = res.pop()
                z = y - x
                res.append(z)
            elif c == "*":
                res.append(res.pop() * res.pop())
            elif c == "/":
                x = res.pop()
                y = res.pop()
                int(z = y / x)
                res.append(z)
            else:
                res.append(int(c))
        return res[0]