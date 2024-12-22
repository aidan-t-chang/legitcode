
def draw_line(n):
    ret = []
    for i in range(n+1):
        ret.append(str(i))

    for i in range(n-1, -1, -1):
        ret.append(str(i))
    
    return ret


def solve():
    n = int(input())
    # n - i spaces
    for i in range(n+1):
        spaces = ""
        for _ in range(n-i):
            spaces += "  "
        two = " ".join(draw_line(i))
        print(spaces + two)
    for i in range(n-1,-1,-1):
        spaces2 = ""
        for _ in range(n-i):
            spaces2 += "  "
        tt = " ".join(draw_line(i))
        print(spaces2 + tt)

    
solve()

    