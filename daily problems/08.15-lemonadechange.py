# At a lemonade stand, each lemonade costs $5. 
# Customers are standing in a queue to buy from you and order one at a time 
# (in the order specified by bills). 
# Each customer will only buy one lemonade and pay with either a $5, 
# $10, or $20 bill. You must provide the correct change to each customer 
# so that the net transaction is that the customer pays $5.

# Note that you do not have any change in hand at first.

# Given an integer array bills where bills[i] is the bill the ith customer 
# pays, return true if you can provide every customer with the correct change,
#  or false otherwise.

class Solution:
    def lemonadeChange(self, bills) -> bool:
        a,b=0,0
        for i in range(len(bills)):
            if bills[i]==5:
                a+=1
            elif bills[i]==10:
                b+=1
                if not a:
                    return False
                a-=1
            else:
                if a and b:
                    a-=1
                    b-=1
                elif a>2:
                    a-=3
                else:
                    return False
        return True