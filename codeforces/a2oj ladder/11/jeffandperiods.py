def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    unique_values = list(set(arr))
    unique_values.sort()
    ind = {val:[] for val in unique_values}
    
    for i, val in enumerate(arr):
        ind[val].append(i)
        
     
    valid = []
    for key in ind:
        temp_arr = ind[key]
        if len(temp_arr) > 1:
            diff = temp_arr[1] - temp_arr[0]
            if all(diff == (temp_arr[i+1] - temp_arr[i]) for i in range(len(temp_arr)-1)):
                valid.append([key, diff])
        else:
            valid.append([key, 0])
    
    print(len(valid))
    for key, diff in valid:
        print(" ".join([str(key), str(diff)]))
        
    


solve()
