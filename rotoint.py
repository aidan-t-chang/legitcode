# Given a roman numeral, convert it to an integer.

dic = {"I":1,
       "IV":4,
       "V":5,
       "IX":9,
       "X":10,
       "XL":40,
       "L":50,
       "XC":90,
       "C":100,
       "CD":400,
       "D":500,
       "CM":900,
       "M":1000
       }

#print(rows("III"))
# print(rows("IV"))
# print(rows("MCMXCIV"))
# print("1476: ", rows("MCDLXXVI"))

f = "MCDLXXVI"
g = f[::-1]
s = [g[i:i+2] for i in range(0, len(g), 2)]

def roman(s):
    counter = 0
    for i in range(0, len(s)):
        if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
            counter -= dic[s[i]]
        else:
            counter += dic[s[i]]
    return counter

print(roman("III"))
print(roman("IV"))
print(roman("MCMXCIV"))
print("1476: ", roman("MCDLXXVI"))




def rows(s):
    counter = 0
    f = s[::-1]
    g = [f[i:i+2] for i in range(0, len(f), 2)]
    for i in g:
        if i[::-1] in dic:
            counter += dic[i[::-1]]
        else:
            for b in i[::-1]:
                counter += dic[b]
    return counter
