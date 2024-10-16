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
    
# don't even do sliding window, just brute force O(n^2)
psum = [0]
for n in arr:
    psum.append(psum[-1]+n)

modArray = []
for n in psum:
    modArray.append(n%7)
    
res = 0
for i in range(len(modArray)):
    for j in range(i, len(modArray)):
        if modArray[i] == modArray[j]:
            res = max(res, abs(j - i))

with open('div7.out', 'w') as fout:
    fout.write(str(res))
            