
from collections import defaultdict

class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda a: a[1])

        # Store queries with their original indices
        sorted_queries = sorted(
            [(q, i) for i, q in enumerate(queries)]
        )

        freq = defaultdict(int)
        ans = [0] * len(queries)

        left = right = 0
        active = 0
        m = len(logs)

        for q, idx in sorted_queries:
            start = q - x

            # Add logs with time <= q
            while right < m and logs[right][1] <= q:
                server = logs[right][0]

                if freq[server] == 0:
                    active += 1

                freq[server] += 1
                right += 1

            # Remove logs with time < q - x
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                freq[server] -= 1

                if freq[server] == 0:
                    active -= 1

                left += 1

            ans[idx] = n - active

        return ans
