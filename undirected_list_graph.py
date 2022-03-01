from typing import List, Set
from collections import defaultdict, deque


class UnDirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edges(self, u: int, vs: List[int]) -> None:
        for v in vs:
            self.graph[u].append(v)
            self.graph[v].append(u)
    
    def dfs(self, src: int, visited: Set[int] = None, ans: List[int] = None) -> List[int]:
        # Recursive
        if visited is None:
            visited = set()
        if ans is None:
            ans = list()
        if src in visited:
            return ans
        visited.add(src)
        ans.append(src)
        for neighbor in self.graph[src]:
            self.dfs(neighbor, visited, ans)
        return ans

    def dfs_2(self, src: int) -> List[int]:
        # Iterative
        visited = set()
        ans = []
        stack = [src]
        while len(stack) > 0:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                ans.append(node)
            for neighbor in self.graph[node][::-1]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return ans

    def bfs(self, src: int) -> List[int]:
        # Iterative
        visited = {src}
        queue = deque([src])
        ans = []
        while len(queue) > 0:
            node = queue.popleft()
            ans.append(node)
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return ans
