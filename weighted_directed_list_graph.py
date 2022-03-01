from typing import List, Set, Dict
from collections import defaultdict, deque
from random import shuffle


class WeightedDirectedGraph:
    def __init__(self):
        self.graph = defaultdict(dict)

    def add_edges(self, u: int, vs: Dict[str, int]) -> None:
        # u -> vs ({v0: w0, v1: w1, ...})
        self.graph[u] = vs

    def get_paths(self, start: str, longest=False) -> Dict[str, int]:
        # Topological sort + DP
        ordering = self.top_sort()
        if len(ordering) != self.count_nodes():
            raise RuntimeError('Detected cycle.')
        dist = dict()
        dist[start] = 0
        for node in ordering:
            if node in dist:
                for nbr, w in self.graph[node].items():
                    new_dist = dist[node] + w if not longest else dist[node] - w
                    dist[nbr] = new_dist if nbr not in dist else min(dist[nbr], new_dist)
        return dist if not longest else dict(map(lambda item: (item[0], -item[1]), dist.items()))

    def get_paths_2(self, start: str, longest=False) -> Dict[str, int]:
        # Bellman–Ford algorithm
        # TODO
        pass
    
    def get_paths_3(self, start: str, longest=False) -> Dict[str, int]:
        # Dijkstra's algorithm
        # TODO
        pass

    def top_sort(self) -> List[str]:
        # Kahn's algorighm
        # Cycle detectable
        incoming_map = defaultdict(int)
        for neighbors in self.graph.values():
            for neighbor in neighbors.keys():
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

    def count_nodes(self) -> int:
        num_nodes = 0
        checked = set()
        for node, neighbors in self.graph.items():
            if node not in checked:
                checked.add(node)
                num_nodes += 1
            for neighbor in neighbors.keys():
                if neighbor not in checked:
                    checked.add(neighbor)
                    num_nodes += 1
        return num_nodes
