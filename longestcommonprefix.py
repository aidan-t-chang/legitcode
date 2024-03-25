# Write a function to find the longest common prefix 
# string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def lcp(strs):
    string = ""
    ticker = False
    counter1 = 0
    counter2 = 0
    for i in range(0, len(strs)):
        print(i)
    return string

f = ["flower","flow","flight"]

s = ""
counter = 0
counter2 = 0
ticks = False
def fortnite(f):
    for i in range(0, len(f)):
        if f[i][counter] in f[i+1][counter2] and i+1 < len(f) - 1 and counter2+1 < len(f) -1:
            counter += 1
            ticks = True
        elif counter+1 == len(f) - 1 and ticks == True:
            s = f[0][0:counter]
        else:
            pass
    return f

t = ["flower","flow","flight"]
print(t[0][0])
print(t[1][0])
print(t[2][0])
print(t[0][1])
print(t[1][1])
print(t[2][1])
g = "fortnite"
h = "for"
