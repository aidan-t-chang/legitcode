"""
ID: your_id_here
LANG: PYTHON3
TASK: bcount
"""

fin = open('bcount.in', 'r')

def psum(arr, id):
    prefix = [0]
    for n in arr:
        if n == id:
            prefix.append(prefix[-1]+1)
        else:
            prefix.append(prefix[-1])
    return prefix

n, q = map(int, fin.readline().split())
arr = []
for i in range(n):
    arr.append(int(fin.readline()))
    # generates the actual array
# print('arr:', arr)
one = psum(arr, 1)
two = psum(arr, 2)
three = psum(arr, 3)
# print('one: ', one, '\ntwo: ', two, '\nthree: ', three)

with open('bcount.out','w') as fout:
    for i in range(q):
        a, b = map(int, fin.readline().split())
        res = ""
        fout.write("{a} {b} {c}\n".format(a=str(one[b]-one[a-1]), b=str(two[b]-two[a-1]), c=str(three[b]-three[a-1])))
