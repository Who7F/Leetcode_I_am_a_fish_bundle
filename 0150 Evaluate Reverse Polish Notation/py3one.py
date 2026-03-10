class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            elif i == "+":
                top = stack.pop() 
                stack.append(stack.pop() + top)
            elif i == "-":
                top = stack.pop() 
                stack.append(stack.pop() - top)
            elif i == "*":
                top = stack.pop() 
                stack.append(stack.pop() * top)
            elif i == "/":
                top = stack.pop() 
                stack.append(int(stack.pop() / top))
            else:
                return -1

        return stack[0]