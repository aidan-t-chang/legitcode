# Given two sorted arrays nums1 and nums2 of size m and n respectively, 
# return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def find(nums1, nums2):
    a, b = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2

    if len(b) < len(a):
        a, b = b, a

    l, r = 0, len(a) - 1
    while True:
        i = (l + r) // 2 # for A
        j = half - i - 2 # pointer for B; j is not number of elements, it is the index number(hence - 2)

        Aleft = a[i] if i >= 0 else float('-infinity')
        Aright = a[i+1] if (i + 1) < len(a) else float('infinity')
        Bleft = b[j] if j >= 0 else float('-infinity')
        Bright = b[j+1] if (j + 1) < len(b) else float('infinity')

        if Aleft <= Bright and Bleft <= Aright: # means the left partition is correct
            if total % 2 == 1: # the number is odd
                return min(Aright, Bright)
            
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
                 
