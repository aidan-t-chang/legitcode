# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

def pal(s):
    n = s.lower()
    news = []
    for i in n:
        if 97 <= ord(i) <= 122 or 48 <= ord(i) <= 57:
            news.append(i)
    return news == news[::-1]

print(pal('Race a car.')) 
print(pal("A man, a plan, a canal: Panama"))
print(pal('0P'))

