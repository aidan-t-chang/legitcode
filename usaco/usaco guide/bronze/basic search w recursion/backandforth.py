import sys
sys.stdin = open("backforth.in", "r")
sys.stdout = open("backforth.out", "w")

def solve():
    barn1 = list(map(int, input().split()))
    barn2 = list(map(int, input().split()))
    res = set()
    def dfs(b1, b2, b1c, b2c, ticker):
        if ticker == 5:
            res.add(b1c)
            return

        for i, bucket in enumerate(b1):
            new_buckets_dest = b2 + [bucket]
            new_buckets_src = [b for j, b in enumerate(b1) if j != i]
            
            new_tank_dest = b2c + bucket
            new_tank_src = b1c - bucket
            
            dfs(new_buckets_dest, new_buckets_src, new_tank_dest, new_tank_src, ticker + 1)

        
    dfs(barn1, barn2, 1000, 1000, 1)
    return len(res)


print(solve())