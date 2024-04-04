# Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.

from collections import defaultdict 

def groupAnagrams(strs):
    ret = defaultdict(list)
    for str in strs:
        count = [0] * 26
        for c in str:
            count[ord(c) - ord('a')] += 1
        ret[tuple(count)].append(str)
    return ret.values()
