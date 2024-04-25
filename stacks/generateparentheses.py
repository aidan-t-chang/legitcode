# Given n pairs of parentheses, 
# write a function to generate all combinations of well-formed parentheses.

def parentheses(n):
    stack = []
    res = []
    def backtrack(openN, closedN):
        if openN == closedN == n: 
            # if the limit n has been reached and there are equal amounts of parentheses
            res.append("".join(stack))
            return

        if openN < n:
            # there are more open parentheses to append
            stack.append('(')
            backtrack(openN + 1, closedN)
            stack.pop()

        if closedN < openN:
            # only condition where a closing parentheses can be appended
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()

    backtrack(0, 0)
    return res