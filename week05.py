def is_valid_brackets(expression: str) -> bool:  # type hint //str = parameter data type, bool = return type
    stack = []
    brackets = {')':'(','}':'{',']':'['}

    for letter in expression:
        if letter in brackets.values():
            stack.append(letter)
        if letter in brackets.keys():
            if not stack or stack.pop() != brackets[letter]:
                return False
    return not stack

print(is_valid_brackets("([2+3)]")) # 스택안에  순서 ( -> [ 인데 찾는것은 ) -> ] 이므로 (,]로 짝이 맞지 않음
print(is_valid_brackets("(2+{3*9})"))
print(is_valid_brackets("(2+(3*9)"))
print(is_valid_brackets(")2+(3*9)("))