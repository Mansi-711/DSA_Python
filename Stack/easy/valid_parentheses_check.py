def valid_parentheses(p):
    stack = []
    check = {']':'[', '}':'{', ')':'('}
    for i in p:
        if i in check.keys():
            if check[i] == stack[-1]:
                stack.pop()
        else:
            stack.append(i)

    return not stack

p = '[{()}]'        
print(valid_parentheses(p))
lis = input('enter a parentheses to check')
print(valid_parentheses(lis))
    
