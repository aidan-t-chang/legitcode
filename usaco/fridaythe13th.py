"""
ID: your_id_here
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
n = int(fin.readline())

dayofweek = {i: 0 for i in range(7)}
months = [31,28,31,30,31,30,31,31,30,31,30,31]
day = 0

for yr in range(1900, 1900+n):
    for month in months:
        dayofweek[day%7] += 1
        if month == 28: # if it is february
            if not (yr%400) or (yr%100 and not yr%4):
                day += 29
                continue
        day += month


with open('friday.out', 'w') as fout:
    for day in range(6):
        fout.write("{} ".format(dayofweek[day]))
    fout.write("{}\n".format(dayofweek[6]))

fout.close()