"""
ID: your_id_here
LANG: PYTHON3
TASK: div7
"""

fin = open('div7.in', 'r')

n = int(fin.readline())

arr = [] # [3,5,1,6,2,14,10]
for i in range(n):
    temp = int(fin.readline())
    arr.append(temp)
    
psum = [0]
for n in arr:
    psum.append(psum[-1]+n)

modArray = []
for n in psum:
    modArray.append(n%7)
    
res = 0
for i in range(7): # optimization: don't need to go through every n for n, just every n for 0-6
    l, r = None, None
    for j in range(len(modArray)): # finding the largest window (sliding window)
        if modArray[j] == i:
            if not l:
                l = j
            r = j
    
    if not r:
        continue
    res = max(res, r - l)

with open('div7.out', 'w') as fout:
    fout.write(str(res))
            