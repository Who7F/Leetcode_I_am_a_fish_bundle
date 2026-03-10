class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+','-','*','/'}

        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                y = stack.pop()
                x = stack.pop()

                match t:
                    case '+':
                        stack.append(x + y)
                    case '-':
                        stack.append(x - y)
                    case '*':
                        stack.append(x * y)
                    case '/':
                        stack.append(int(x / y))


        return stack.pop()