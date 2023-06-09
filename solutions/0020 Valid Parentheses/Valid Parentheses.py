def isValid(s):
    if len(s) % 2 != 0:
        return False
    
    table = {"(" : ")", "{": "}",  "[": "]"}
    stack = []
    
    for char in s:
        if char in table:
            stack.append(char)
        else:
            if not stack:
                return False
            # stack is LIFO
            top_of_stack = stack.pop()
            if char != table[top_of_stack]:
                return False
            
    return len(stack) == 0