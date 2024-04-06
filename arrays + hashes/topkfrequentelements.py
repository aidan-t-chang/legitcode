# Given an integer array nums and an integer k, 
# return the k most frequent elements. You may return the answer in any order.'

def frequent(nums, k):
    hash = {}
    frequency = [[] for i in range(len(nums) + 1)] # initializing the array with empty arrays for every count 
    
    for i in nums:
        hash[i] = 1 + hash.get(i, 0) # count how many times each value in nums occurs (hash.get)
    for num, count in hash.items():
        frequency[count].append(num) # this value num appears exactly count number of times
    
    ret = []
    for i in range(len(frequency) - 1, 0, -1): #working through the frequency array through descending order (0, -1 causes reverse iteration)
        for n in frequency[i]: # for every array within the array of frequency
            ret.append(n)
            if len(ret) == k: # stopper condition for when we find the top k frequent elements
                return ret

# (lines 16 and 17) for the most frequent value, append that value to ret. when ret eventually has k elements, we return ret