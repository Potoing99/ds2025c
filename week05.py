def check_parentheses(expression : str) -> bool: #type hint //str = parameter data type, bool = return type
    stack = []
    for letter in expression:
        if letter == "(":
            stack.append(letter)
        if letter == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(check_parentheses("(2+3)"))
print(check_parentheses("(2+(3*9))"))
print(check_parentheses("(2+(3*9)"))
print(check_parentheses(")2+(3*9)("))