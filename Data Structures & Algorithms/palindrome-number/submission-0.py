class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        origX = x
        res = 0
        while x > 0:
            digit = x % 10
            res *= 10
            res += digit
            x //= 10
        return res == origX
        