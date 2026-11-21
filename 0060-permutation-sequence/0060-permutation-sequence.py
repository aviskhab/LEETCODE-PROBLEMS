
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]

        # Precompute factorials
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i

        # Convert k to zero-based indexing
        k -= 1

        ans = ""

        while nums:
            # Find the index of the next number
            index = k // fact[len(nums) - 1]

            ans += nums.pop(index)

            # Update k for the remaining permutations
            k %= fact[len(nums)]

        return ans
