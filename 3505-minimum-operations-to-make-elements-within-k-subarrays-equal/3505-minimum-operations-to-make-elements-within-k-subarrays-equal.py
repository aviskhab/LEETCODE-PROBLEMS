import heapq
from collections import defaultdict

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)

        left = []   # Max heap (negative values)
        right = []  # Min heap

        delayed = defaultdict(int)
        sum_left = sum_right = 0
        size_left = size_right = 0

        def prune(heap, sign):
            while heap:
                v = heap[0] * sign
                if delayed[v]:
                    delayed[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def rebalance():
            nonlocal size_left, size_right
            nonlocal sum_left, sum_right

            prune(left, -1)
            prune(right, 1)

            while size_left > size_right + 1:
                prune(left, -1)
                v = -heapq.heappop(left)
                size_left -= 1
                size_right += 1
                sum_left -= v
                sum_right += v
                heapq.heappush(right, v)

            while size_left < size_right:
                prune(right, 1)
                v = heapq.heappop(right)
                size_right -= 1
                size_left += 1
                sum_right -= v
                sum_left += v
                heapq.heappush(left, -v)

        def add(v):
            nonlocal size_left, size_right
            nonlocal sum_left, sum_right

            prune(left, -1)

            if not left or v <= -left[0]:
                heapq.heappush(left, -v)
                size_left += 1
                sum_left += v
            else:
                heapq.heappush(right, v)
                size_right += 1
                sum_right += v

            rebalance()

        def remove(v):
            nonlocal size_left, size_right
            nonlocal sum_left, sum_right

            prune(left, -1)
            prune(right, 1)

            delayed[v] += 1

            if v <= -left[0]:
                size_left -= 1
                sum_left -= v
                if v == -left[0]:
                    prune(left, -1)
            else:
                size_right -= 1
                sum_right -= v
                if right and v == right[0]:
                    prune(right, 1)

            rebalance()

        def get_cost():
            prune(left, -1)
            m = -left[0]
            return m * size_left - sum_left + sum_right - m * size_right

        costs = []

        for i in range(n):
            add(nums[i])

            if i >= x:
                remove(nums[i - x])

            if i >= x - 1:
                costs.append(get_cost())

        # DP
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]