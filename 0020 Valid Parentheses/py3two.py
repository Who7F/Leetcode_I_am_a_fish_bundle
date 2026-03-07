class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'{':'}','[':']','(':')'}
        stack = []
        for i in s:
            if i in pairs:
                stack.append(pairs[i])
            elif not stack or stack.pop() != i:
                return False
                
        return not stack
