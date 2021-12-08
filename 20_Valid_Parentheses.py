def isValid(s):
    stack = []
    for c in s:
        if c in ['(', '{', '[']:
            stack.append(c)
        elif c == ")":
            if len(stack) != 0 and stack[-1] == "(":
                stack.pop()
            else:
                return False
        elif c == "}":
            if len(stack) != 0 and stack[-1] == "{":
                stack.pop()
            else:
                return False
        elif c == "]":
            if len(stack) != 0 and stack[-1] == "[":
                stack.pop()
            else:
                return False
        else:
            return False
    return not bool(len(stack))

def test():
    print(isValid("()"))

test()