# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!

class Solution:
    def decrypt(self, code, k: int):
        n=len(code)
        ans=[0]*n
        if k==0: return ans
        if k>0:
            ans[0]=wsum=sum(code[1:k+1])
            for l in range(1, n):
                r=(l+k)%n
                wsum+=-code[l]+code[r]
                ans[l]=wsum
            return ans
        # Python has minus index
        ans[0]=wsum=sum(code[-1:k-1:-1])
        for l in range(1, n):
            r=(l-k)%n
            wsum+=-code[-l]+code[-r]
            ans[-l]=wsum
        return ans