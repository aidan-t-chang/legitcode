n = int(input())
weights = list(map(int, input().split()))

def backtrack(i, sum1, sum2):
	if i == n:
		return abs(sum2 - sum1)

	return min(backtrack(i + 1, sum1 + weights[i], sum2), backtrack(i + 1, sum1, sum2 + weights[i]))
print(backtrack(0, 0, 0))