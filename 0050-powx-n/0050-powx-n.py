class Solution:
    def myPow(self, x: float, n: int) -> float:
        power = abs(n)
        ans = 1.0

        while power > 0:
            if power % 2 == 1:
                ans *= x

            x *= x
            power //= 2

        if n < 0:
            return 1.0 / ans

        return ans