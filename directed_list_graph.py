from typing import List, Set, Dict
from collections import defaultdict, deque
from random import shuffle


class DirectedGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edges(self, u: int, vs: List[int]) -> None:
        # u -> vs (v0, v1, ...)
        self.graph[u] = vs
    
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

    def get_path(self, start: int, end: int) -> List[int]:
        # BFS
        def bfs(s: int) -> Dict[int, int]:
            visited = {s}
            queue = deque([start])
            ans = dict()
            while len(queue) > 0:
                node = queue.popleft()
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
                        ans[neighbor] = node
            return ans

        prev_map = bfs(start)
        path = []
        at = end
        while True:
            path.append(at)
            if at in prev_map:
                at = prev_map[at]
            else:
                break
        path.reverse()
        return path if path[0] == start else []

    def top_sort(self) -> List[int]:
        # Kahn's algorighm
        # Cycle detectable
        incoming_map = defaultdict(int)
        for neighbors in self.graph.values():
            for neighbor in neighbors:
                incoming_map[neighbor] += 1
        
        no_incomings = []
        for node in self.graph.keys():
            if node not in incoming_map:
                no_incomings.append(node)

        ans = []
        while len(no_incomings) > 0:
            node = no_incomings.pop()
            ans.append(node)
            for neighbor in self.graph[node]:
                incoming_map[neighbor] -= 1
                if incoming_map[neighbor] <= 0:
                    no_incomings.append(neighbor)
        return ans

    def top_sort_2(self) -> List[int]:
        # DFS
        def dfs(src: str):
            if src in visited:
                return
            visited.add(src)
            for neighbor in self.graph[src]:
                dfs(neighbor)
            ans.append(src)

        visited = set()
        ans = []
        nodes = list(self.graph)
        for node in nodes:
            dfs(node)
        ans.reverse()
        return ans

    def top_sort_3(self) -> List[int]:
        # DFS
        # Cycle detectable
        def dfs(src: str) -> bool:
            # Return false when a cycle is detected.
            if src in permanent:
                return False
            if src in temporary:
                return True
            temporary.add(src)
            for neighbor in self.graph[src]:
                if dfs(neighbor):
                    return True
            temporary.remove(src)
            permanent.add(src)
            ans.append(src)
            return False

        temporary = set()
        permanent = set()
        ans = []
        nodes = list(self.graph)
        for node in nodes:
            if dfs(node):
                # Abort because it's not a DAG.
                return ans
        ans.reverse()
        return ans
 
    def count_nodes(self) -> int:
        num_nodes = 0
        checked = set()
        for node, neighbors in self.graph.items():
            if node not in checked:
                checked.add(node)
                num_nodes += 1
            for neighbor in neighbors:
                if neighbor not in checked:
                    checked.add(neighbor)
                    num_nodes += 1
        return num_nodes

    def is_dag(self) -> bool:
        # Use top_sort()
        return self.count_nodes() == len(self.top_sort())

    def is_dag_2(self) -> bool:
        # Use top_sort_3()
        return self.count_nodes() == len(self.top_sort_3())
