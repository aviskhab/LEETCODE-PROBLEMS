class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        n = len(nums)

        if all(nums[i] == i for i in range(n)):
            return 0

        ans = (1 << 31) - 1

        for i in range(n):
            if nums[i] != i:
                ans &= nums[i] & i

        return ans