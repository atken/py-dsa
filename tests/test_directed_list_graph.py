from directed_list_graph import DirectedGraph


def test_dfs():
    """
    0 → 1 → 2 → 5
    ↓     ↗
    3 → 4 → 6
    """
    g = DirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [5])
    g.add_edges(3, [4])
    g.add_edges(4, [2, 6])
    
    assert g.dfs(0) == g.dfs_2(0) == [0, 1, 2, 5, 3, 4, 6]
    assert g.dfs(2) == g.dfs_2(2) == [2, 5]
    assert g.dfs(4) == g.dfs_2(4) == [4, 2, 5, 6]

def test_bfs():
    """
    0 → 1 → 2 → 5
    ↓     ↗
    3 → 4 → 6
    """
    g = DirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [5])
    g.add_edges(3, [4])
    g.add_edges(4, [2, 6])
  
    assert g.bfs(0) == [0, 1, 3, 2, 4, 5, 6]
    assert g.bfs(2) == [2, 5]
    assert g.bfs(4) == [4, 2, 6, 5]

def test_get_path():
    """
    0 → 1 → 2 → 5
    ↓     ↗
    3 → 4 → 6
          ↘
            7 → 8
    """
    g = DirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [5])
    g.add_edges(3, [4])
    g.add_edges(4, [2, 6, 7])
    g.add_edges(7, [8])
  
    assert g.get_path(0, 6) == [0, 3, 4, 6]
    assert g.get_path(1, 7) == []
    assert g.get_path(3, 8) == [3, 4, 7, 8]

def test_top_sort():
    """
    0 → 1 → 2 → 5
    ↓ ↗   ↗
    3 → 4 → 6
    """
    g = DirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [5])
    g.add_edges(3, [1, 4])
    g.add_edges(4, [2, 6])
    
    assert g.top_sort() == [0, 3, 4, 6, 1, 2, 5]
 
def test_top_sort_2():
    """
    0 → 1 → 2 → 5
    ↓ ↗   ↗
    3 → 4 → 6
    """
    g = DirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [5])
    g.add_edges(3, [1, 4])
    g.add_edges(4, [2, 6])
    
    assert g.top_sort_2() == [0, 3, 4, 6, 1, 2, 5]

def test_top_sort_3():
    """
    0 → 1 → 2 → 5
    ↓ ↗   ↗
    3 → 4 → 6
    """
    g = DirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [5])
    g.add_edges(3, [1, 4])
    g.add_edges(4, [2, 6])
    
    assert g.top_sort_3() == [0, 3, 4, 6, 1, 2, 5]

def test_is_dag():
    """
    0 → 1 → 2 → 5
    ↓ ↗   ↗
    3 → 4 → 6
    """
    g = DirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [5])
    g.add_edges(3, [1, 4])
    g.add_edges(4, [2, 6])
    
    assert g.is_dag() == True
    assert g.is_dag_2() == True

def test_is_dag_cycle():
    """
    0 → 1 → 2 → 5
    ↓ ↗   ↗ ↓
    3 → 4 ← 6
    """
    g = DirectedGraph()
    g.add_edges(0, [1, 3])
    g.add_edges(1, [2])
    g.add_edges(2, [5, 6])
    g.add_edges(3, [1, 4])
    g.add_edges(4, [2])
    g.add_edges(6, [4])
    
    assert g.is_dag() == False
    assert g.is_dag_2() == False

