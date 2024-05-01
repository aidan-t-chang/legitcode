# You are given an array of strings tokens that represents an arithmetic expression in 
# a Reverse Polish Notation.
# Evaluate the expression. 
# Return an integer that represents the value of the expression.

def evalRPN(tokens):
    newstack = []
    for token in tokens:
        if token == "+":
            newstack.append(newstack.pop()+newstack.pop())
        elif token == "-":
            a, b = newstack.pop(), newstack.pop()
            newstack.append(b-a)
        elif token == "*":
            newstack.append(newstack.pop()*newstack.pop())
        elif token == "/":
            a, b = newstack.pop(), newstack.pop()
            newstack.append(int(b/a))
        else:
            newstack.append(int(token))
        return newstack[0]