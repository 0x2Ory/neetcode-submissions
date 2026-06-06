class Solution:
    def isValid(self, s: str) -> bool:
        dictBrack = {'[':']', '{': '}', '(':')'}
        stack = []
        for char in s:
            if(char in dictBrack):
                stack.append(char)
            else:
                if not stack: 
                    return False
                if dictBrack[stack.pop()] != char:
                    return False

        return True