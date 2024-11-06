"""
ID: your_id_here
LANG: PYTHON3
TASK: hps
"""

read = open("hps.in", "r").readline
write = open("hps.out", "w").write

n, ans = int(read()), 0

pref = [[0 for _ in range(n)] for _ in range(3)]

H, P, S = 0, 1, 2
h, p, s = 0, 0, 0

for i in range(n):
    ch = read()[0]
    if ch == 'H':
        h += 1
    elif ch == 'P':
        p += 1
    elif ch == 'S':
        s += 1
    pref[H][i] = h
    pref[P][i] = p
    pref[S][i] = s
    
for i in range(n):
    max_left, max_right = 0, 0
    for j in range(3):
        max_left = max(max_left, pref[j][i])
        max_right = max(max_right, pref[j][n - 1] - pref[j][i])
    ans = max(ans, max_left + max_right)
write(str(ans))