def valid_parentheses(p):
    stack = []
    d = {']':'[', '}':'{', ')':'('}
    st = ['(','{','[']
    for i in p:
        if not len(stack) and i not in st:
            return False
        if not len(stack) and i in d:
            return False
        if i in d and d[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    return not stack

p = '[{()}]'        
print(valid_parentheses(p))
lis = input('enter a parentheses to check: ')
print(valid_parentheses(lis))
    
