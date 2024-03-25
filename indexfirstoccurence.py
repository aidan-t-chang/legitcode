# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

def firstocc(haystack, needle):
    counter = 0
    leng = len(needle)
    cond = False
    if needle not in haystack:
        return -1
    else:
        while cond == False:
            if haystack[counter:counter+leng] == needle:
                return counter
            else:
                counter += 1

    

print(firstocc("fortnite", 'forta'))
print(firstocc('fortnite', 'fort'))
print(firstocc('aaafortnite', 'fortnite'), ': 3')