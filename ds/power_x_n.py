class Solution:
    def myPow(self, x: float, n: int) -> float:
        #solution using interation
        #base case 
        if n == 0:
            return 1
        # for negative case
        if n < 0:
            n = -1 * n
            x = 1.0 / x
        
        # This step will do binary exponentiation
        result = 1
        while n != 0:
            if n % 2 == 1:
                result *= x
                n = n -1
            x *= x 
            n // 2
        return result
    
    def binaryExp(x, n):
        return self.myPow(x,n)
