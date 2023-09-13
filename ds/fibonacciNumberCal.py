class Solution:
    #define cache
    cache = {0:0, 1:1}
    def fib(self, N: int) -> int:
        # top-down approach using memoization
        if N in self.cache:
            return self.cache[N]
        self.cache[N] = self.fib(N -1) + self.fib(N -2)
        return self.cache[N]
        
