"""
ID: your_id_here
LANG: PYTHON3
TASK: ride
"""
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
x = fin.readline() # COMETQ
y = fin.readline() # HVNGAT

lea = 1
b = 1
for i in x:
    lea = lea * (ord(i) - 64)

for a in y:
    b = b * (ord(a) - 64)

if lea % 47 == b % 47:
    fout.write("GO" + '\n')
else:
    fout.write("STAY" + '\n')

fout.close()