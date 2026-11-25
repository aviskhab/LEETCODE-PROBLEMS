
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        # Coordinate compression
        vals = {v: i for i, v in enumerate(sorted(set(nums)))}
        arr = [vals[x] for x in nums]

        # Build suffix array using doubling
        sa = list(range(n))
        rank = arr[:]
        k = 1

        while k < n:
            sa.sort(key=lambda i: (
                rank[i],
                rank[i + k] if i + k < n else -1
            ))

            new_rank = [0] * n

            for j in range(1, n):
                a, b = sa[j - 1], sa[j]

                prev = (
                    rank[a],
                    rank[a + k] if a + k < n else -1
                )
                curr = (
                    rank[b],
                    rank[b + k] if b + k < n else -1
                )

                new_rank[b] = new_rank[a] + (prev != curr)

            rank = new_rank

            if rank[sa[-1]] == n - 1:
                break

            k *= 2

        # Build inverse suffix array
        pos = [0] * n
        for i, s in enumerate(sa):
            pos[s] = i

        # Kasai LCP
        lcp = [0] * n
        h = 0

        for i in range(n):
            p = pos[i]

            if p == 0:
                continue

            j = sa[p - 1]

            while (i + h < n and j + h < n
                   and nums[i + h] == nums[j + h]):
                h += 1

            lcp[p] = h
            h = max(0, h - 1)

        # Maximum LCP with either neighboring suffix
        best = n

        for i in range(n):
            common = max(
                lcp[i],
                lcp[i + 1] if i + 1 < n else 0
            )

            if common < n - sa[i]:
                best = min(best, common + 1)

        return best
