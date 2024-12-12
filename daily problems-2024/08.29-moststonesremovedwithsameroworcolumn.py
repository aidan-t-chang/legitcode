# On a 2D plane, we place n stones at some integer coordinate points. 
# Each coordinate point may have at most one stone.

# A stone can be removed if it shares either the same row or the same 
# column as another stone that has not been removed.

# Given an array stones of length n where stones[i] = [xi, yi] represents 
# the location of the ith stone, return the largest possible number of 
# stones that can be removed.


class Solution:
    def removeStones(self, stones) -> int:
        n, M=len(stones), 10001
        N=2*M+1
        root=list(range(N))
        Size=[1]*N
        merge=0

        def Find(x):
            if x==root[x]: return x
            root[x]=Find(root[x])
            return root[x]
        
        def Union(x, y):
            nonlocal merge
            x, y=Find(x), Find(y)
            if x==y: return False
            if Size[x]>Size[y]:
                Size[x]+=Size[y]
                root[y]=x
            else:
                Size[y]+=Size[x]
                root[x]=y
            merge+=1
            return True
        cntRC=[False]*N
        for i, j in stones:
            Union(i, M+j)
            cntRC[i]=cntRC[M+j]=True
        return n-cntRC.count(True)+merge
