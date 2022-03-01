from undirected_list_graph import UnDirectedGraph


def test_dfs():
    r"""
    0-1-2-5   0: [1, 3]
     \  |     1: [0, 2]
      3-4-6   2: [1, 4, 5]
              3: [0, 4]
              4: [2, 3, 6]
              5: [2]
              6: [4] 
    """
    g = UnDirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [4, 5])
    g.add_edges(3, [4])
    g.add_edges(4, [6])
    
    assert g.dfs(0) == g.dfs_2(0) == [0, 1, 2, 4, 3, 6, 5]
    assert g.dfs(2) == g.dfs_2(2) == [2, 1, 0, 3, 4, 6, 5]
    assert g.dfs(5) == g.dfs_2(5) == [5, 2, 1, 0, 3, 4, 6]

def test_bfs():
    r"""
    0-1-2-5   0: [1, 3]
     \  |     1: [0, 2]
      3-4-6   2: [1, 4, 5]
              3: [0, 4]
              4: [2, 3, 6]
              5: [2]
              6: [4] 
    """
    g = UnDirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [4, 5])
    g.add_edges(3, [4])
    g.add_edges(4, [6])
    
    assert g.bfs(0) == [0, 1, 3, 2, 4, 5, 6]
    assert g.bfs(2) == [2, 1, 4, 5, 0, 3, 6]
    assert g.bfs(5) == [5, 2, 1, 4, 0, 3, 6]

