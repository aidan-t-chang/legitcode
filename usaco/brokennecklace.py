"""
ID: your_id_here
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
n = int(fin.readline())
beads = str(fin.readline())


# sliding window - longest common substring including w?
# two pass; one for all r, one for all b?
# basically longest common substring except with just one bead color
def max_beads(beads):
    n = len(beads)
    beads = beads + beads  # Double the string to simulate circular behavior

    max_beads_collected = 0

    for i in range(n):
        # First, collect beads to the right (clockwise)
        right_color = None
        right_count = 0
        for j in range(i, i + n):
            if beads[j] == 'w' or right_color == beads[j] or right_color is None:
                right_count += 1
                if beads[j] != 'w':
                    right_color = beads[j]
            else:
                break

        # Then, collect beads to the left (counterclockwise)
        left_color = None
        left_count = 0
        for j in range(i - 1, i - n - 1, -1):
            if beads[j] == 'w' or left_color == beads[j] or left_color is None:
                left_count += 1
                if beads[j] != 'w':
                    left_color = beads[j]
            else:
                break

        # Since we can collect at most n beads (the original necklace length)
        total = min(n, left_count + right_count)
        max_beads_collected = max(max_beads_collected, total)

    return max_beads_collected


ans = max_beads(beads)

with open('beads.out', 'w') as fout:
    fout.write(str(ans))

fout.close()