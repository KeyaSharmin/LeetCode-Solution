class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x,y=0,0
        l=[]
        for i in s:
            if i=="N":
                y+=1
            elif i=="W":
                x-=1
            elif i=="S":
                y-=1
            else:
                x+=1
            l.append((abs(x)+abs(y)))
        n=len(l)
        i=1
        c=0
        mx=l[1]
        pre=l[0]
        if k==0:
            return max(l)
        while(i<n):         
           if l[i]<pre and k>0:
               c+=2
               k-=1
           pre=l[i]
           l[i]+=c
           mx=max(mx,l[i])
           i+=1
        return mx
