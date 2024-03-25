# Given a string s containing just the characters 
# '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

def validstring(s):
    if len(s) % 2 != 0:
        return False
    stack = []
    for c in s:
        if c == '(':
            stack.append(')')
        if c == '[':
            stack.append(']')
        if c == '{':
            stack.append('}')    
        if c == ')' or c == ']' or c == '}':
            if len(stack) == 0:
                return False
            else:
                if stack.pop() != c:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False

            


print('check1', validstring('()')) # = true
print('check2', validstring('[])(')) # = false
print('check3', validstring('()[]}{')) # = false
print('check4', validstring("([)]")) # = false
print('check5', validstring('([])')) # = True


f = ['f', 'g', 'a']
f.append('Fortnite')
# print(f.pop())

def varsity(s):
    check1 = 0
    check2 = 0
    check3 = 0
    for i in range(0, len(s)):
        if s[i] == '(':
            check1 = i
        if s[i] == '{':
            check2 = i
        if s[i] == '[':
            check3 = i
        if s[i] == ')' and i > check1:
            check1 = -1
        if s[i] == '}' and i > check2:
            check2 = -2
        if s[i] == ']' and i > check3:
            check3 = -3
    if check1 == 1 or check2 == 1 or check3 == 1:
        return False
    else:
        return True
        