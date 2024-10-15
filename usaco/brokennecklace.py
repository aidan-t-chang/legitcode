"""
ID: your_id_here
LANG: PYTHON3
TASK: friday
"""

fin = open('beads.in', 'r')
n = int(fin.readline())
beads = str(fin.readline())


# sliding window - longest common substring including w?
# two pass; one for all r, one for all b?
# basically longest common substring except with just one bead color

l = 0
# first iteration will be for red beads
for r in range(len(beads)):
    if beads[r] == 'b':
        pass