def isValid(s):
    last = s[0]
    checker = [0,0,0]   # [(), {}, []]
    stack =[]
    if len(s) % 2 != 0:
        return False
    if s[0] in [')','}',']']:
        return False
    for i in range(len(s)):
        if last == '(' and i != len(s) - 1:
            if s[i] == '}' or s[i] == ']':
                return False
        elif last == '{' and i != len(s) - 1:
            if s[i] == ')' or s[i] == ']':
                return False
        elif last == '[' and i != len(s) - 1:
            if s[i] == ')' or s[i] == '}':
                return False
        
        last = s[i]

        if s[i] == '(':
            checker[0] += 1
            stack.append('(')
        elif s[i] == '{':
            checker[1] += 1
            stack.append('{')
        elif s[i] == '[':
            checker[2] += 1
            stack.append('[')
        elif s[i] == ')':
            checker[0] -= 1
            if min(checker) < 0:
                return False
            if stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif s[i] == '}':
            checker[1] -= 1
            if min(checker) < 0:
                return False
            if stack[-1] != '{':
                return False
            else:
                stack.pop()
        elif s[i] == ']':
            checker[2] -= 1
            if min(checker) < 0:
                return False
            if stack[-1] != '[':
                return False
            else:
                stack.pop()
        
    if sum(checker) == 0:
        return True
    else:
        return False


def test():
    print(isValid("()"))

test()