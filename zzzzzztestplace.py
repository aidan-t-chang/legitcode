def func1(n):
    def func2(n):
        return n+3

    print('tester', func2(n+1))


func1(4)
