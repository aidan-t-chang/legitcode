def solve():
    n, m = map(int, input().split())
    correct = list(map(int, input().split()))
    wrong = list(map(int, input().split()))
    
    correct.sort()
    wrong.sort()
    
    # weed out false cases
    
    for i in range(len(correct)-1,-1,-1):
        if correct[i] in wrong:
            return -1
    
    if correct[0] * 2 > wrong[0]:
        return -1

    for i in range(correct[0]+1, wrong[0]):
        if i/2 < wrong[0] and i/2 >= correct[0] and i >= correct[-1]:
            return i
        
    return -1


print(solve())