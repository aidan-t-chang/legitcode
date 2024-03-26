def func1(n):
    def func2(n):
        return n+3

    print('tester', func2(n+1))


func1(4)

arr = [1,2,3,4,5]
# print(arr[len(arr)-1])

g = 'welcome to the jungle'
f = g.split()

print(f[-1])