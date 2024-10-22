class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0) or (x != 0 and x % 10 == 0):
            return False
        temp = 0    
        while x > temp:
            temp = (temp * 10) + (x % 10)
            x = x // 10
        
        return x == temp or x == temp // 10