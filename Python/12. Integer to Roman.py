class Solution:
    def intToRoman(self, num):
        r=''
        d=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        for i,j in d:
            while num>=i:
                r+=j
                num-=i
        return(r)
num=1994
r=Solution().intToRoman(num)
print(r) 
