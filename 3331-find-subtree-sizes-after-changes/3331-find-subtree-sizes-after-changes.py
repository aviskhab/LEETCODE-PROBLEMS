
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        # Store the nearest ancestor for each character
        last = [-1] * 26

        # Final parent array
        new_parent = parent[:]

        def dfs(node):
            c = ord(s[node]) - ord('a')

            # Save the previous nearest ancestor
            prev = last[c]

            # Update the parent if a matching ancestor exists
            if prev != -1:
                new_parent[node] = prev

            # Current node becomes the nearest ancestor
            last[c] = node

            # Traverse original children
            for child in children[node]:
                dfs(child)

            # Restore the previous ancestor (backtracking)
            last[c] = prev

        dfs(0)

        # Build the final tree
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes in the final tree
        answer = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer
