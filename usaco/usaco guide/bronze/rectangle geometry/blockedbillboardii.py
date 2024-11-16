import sys

sys.stdin = open("billboard.in", "r")
sys.stdout = open("billboard.out", "w")


blx, bly, trx, tr_y = map(int, input().split()) #lawnmower billboard
blcf_x, blcf_y, trcf_x, trcf_y = map(int, input().split()) #cow feed billboard

#first, find if cow feed billboard covers 2/4 corners of the lawnmower billboard
# pure casework?


# case 1: the cow feed billboard is covering the rightmost corners
if (blcf_x < trx < trcf_x) and (blcf_y < bly <= tr_y < trcf_y):
    #find the new topright value
    new_tr = [blcf_x, tr_y]
    print(max(0, (new_tr[0] - blx) * (new_tr[1] - bly)))
#case 2: the cow feed billboard is covering the bottom-most corners
elif (blcf_x < blx <= trx < trcf_x) and (blcf_y < bly < trcf_y):
    #find the new bottom left value
    new_bl = [blx, trcf_y]
    print((trx - new_bl[0]) * (tr_y - new_bl[1]))
#case 3: the cow feed billboard is covering the leftmost corners
elif (blcf_x < blx < trcf_x) and (blcf_y < bly <= tr_y < trcf_y):
    new_bl = [trcf_x, bly]
    print((trx - new_bl[0]) * (tr_y - new_bl[1]))
# case 4: the cow feed billboard is covering the top-most corners
elif (blcf_x < blx <= trx < trcf_x) and (blcf_y < tr_y < trcf_y):
    new_tr = [trx, blcf_y]
    print((new_tr[0] - blx) * (new_tr[1] - bly))
# case 5: only one of the corners is covered
else:
    # the entire billboard still needs to be covered
    print((tr_y - bly) * (trx - blx))
    
 