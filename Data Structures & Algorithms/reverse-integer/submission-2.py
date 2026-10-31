class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0
        while x > 0:
            res *= 10
            digit = x % 10
            res += digit
            x //= 10
        if -(1 << 31) <= sign*res <= 1<<31:
            return sign * res
        else:
            return 0
        
        