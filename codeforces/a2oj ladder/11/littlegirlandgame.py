from collections import defaultdict
    
# there can be at most 1 odd count
# optimal to take from the odds until there is two left
# in this case, remove from evens to create more odds
# in a case of all odds, the only case that creates a palindrome is when there is one char
def solve():
    s = input()
    count = defaultdict(int)
    
    for i in range(len(s)):
        count[s[i]] += 1
        
    n = 0
    odds = 0
    for c in count:
        if count[c] % 2:
            odds += 1
        n += 1
    if odds == 1 or odds == 0:
        return "First"
    
    evens = n - odds
    counter = evens + n


    return "First" if counter % 2 else "Second"


print(solve())