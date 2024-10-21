"""
ID: your_id_here
LANG: PYTHON3
TASK: hps
"""


fin = open('hps.in', 'r')
N = int(fin.readline())
arr = []
for i in range(N):
    temp = fin.readline()
    arr.append(temp)
    
h, p, s = [0], [0], [0]

for n in arr:
    if n == "H":
        h.append(h[-1]+1)
        p.append(p[-1])
        s.append(s[-1])
    elif n == "P":
        p.append(p[-1]+1)
        h.append(h[-1])
        s.append(s[-1])
    elif n == "S":
        s.append(s[-1]+1)
        p.append(p[-1])
        h.append(h[-1])
    

with open('hps.out', 'w') as fout:
    pass