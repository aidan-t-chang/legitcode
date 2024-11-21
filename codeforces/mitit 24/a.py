t = int(input())

for i in range(t):
    s = input()
    f = False
    start_idx = 1 if len(s) % 2 else 2
    for partition in range(start_idx, len(s), 2):
        temp = s[partition:]
        left = temp[:len(temp)//2]
        right = temp[len(temp)//2:]
        
        if left == right:
            print('yes')
            f = True
            break
    if f == False:
        print('no')
    
