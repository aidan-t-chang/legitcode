def solve():
    n = int(input())
    nums = list(map(int, input().split()))

    res = 0 
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            count = 0
            for k in range(len(nums)):
                if i <= k and k <= j:
                    count += (1 - nums[k])
                else:
                    count += nums[k]
            res = max(res, count)
    return res
print(solve())

        
