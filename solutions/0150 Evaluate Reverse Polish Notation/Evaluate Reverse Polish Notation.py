def evalRPN(tokens):
    def eval(first, second, op):
        if op == "+":
            return first + second
        elif op == "-":
            return first - second
        elif op == "*":
            return first * second
        else:
            return int(first / second)
    
    stack = []
    operators = ["+", "-", "*", "/"]
    
    for char in tokens:
        if char not in operators:
            stack.append(int(char))
        else:
            second = stack.pop()
            first = stack.pop()
            new_value = eval(first, second, char)
            stack.append(new_value)
            
    return stack[0]