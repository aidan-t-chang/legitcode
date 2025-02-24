import sys

sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out", "w")

n = int(input())
arr = []
for _ in range(n):
    isn = int(input())
    arr.append(isn)

arr.sort()

    
def solve(start, direction):
    radius = 1
    prev = start
    while True:
        next_ = prev
        while (0 <= next_ + direction < len(arr) and abs(arr[next_ + direction] - arr[prev]) <= radius):
            next_ += direction
		# We didn't find a new haybale, so the chain explosion is over
        if next_ == prev:
            break

		# Update our previous explosion and increment radius
        prev = next_
        radius += 1
    return abs(prev - start)

max1 = 0
for i in range(len(arr)):
    max1 = max(max1, solve(i, 1) + solve(i, -1) + 1)
print(max1)