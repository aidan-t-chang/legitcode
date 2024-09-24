"""
ID: your_id_here
LANG: PYTHON3
TASK: friday
"""

fin = open('beads.in', 'r')
n = int(fin.readline())
beads = str(fin.readline())


# sliding window - longest common substring?

l, r = 0, 0
