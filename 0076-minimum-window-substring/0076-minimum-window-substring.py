
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t)
        required = len(t)

        left = 0
        min_len = float('inf')
        start = 0

        for right in range(len(s)):
            if need[s[right]] > 0:
                required -= 1

            need[s[right]] -= 1

            # All characters are included
            while required == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # Remove left character
                need[s[left]] += 1

                if need[s[left]] > 0:
                    required += 1

                left += 1

        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
