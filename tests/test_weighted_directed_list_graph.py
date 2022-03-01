import pytest
from weighted_directed_list_graph import WeightedDirectedGraph


def test_top_sort():
    """
    A →(6)→ B →(2)→ C →(3)→ F
    ↓     ↗       ↗
   (3) (2)     (4)
    ↓ ➚       ➚
    D →(1)→ E →(5)→ G
    """
    g = WeightedDirectedGraph()
    g.add_edges('A', {'B': 6, 'D': 3})
    g.add_edges('B', {'C': 2})
    g.add_edges('C', {'F': 3})
    g.add_edges('D', {'B': 2, 'E': 1})
    g.add_edges('E', {'C': 4, 'G': 5})
    
    assert g.top_sort() == ['A', 'D', 'E', 'G', 'B', 'C', 'F']

def test_get_paths():
    """
    A →(6)→ B →(2)→ C →(3)→ F
    ↓     ↗       ↗
   (3) (2)     (4)
    ↓ ➚       ➚
    D →(1)→ E →(5)→ G
    """
    g = WeightedDirectedGraph()
    g.add_edges('A', {'B': 6, 'D': 3})
    g.add_edges('B', {'C': 2})
    g.add_edges('C', {'F': 3})
    g.add_edges('D', {'B': 2, 'E': 1})
    g.add_edges('E', {'C': 4, 'G': 5})
    
    sp_map = g.get_paths('A')
    assert sp_map['A'] == 0
    assert sp_map['B'] == 5
    assert sp_map['C'] == 7
    assert sp_map['D'] == 3
    assert sp_map['E'] == 4
    assert sp_map['F'] == 10
    assert sp_map['G'] == 9
    
    sp_map = g.get_paths('D')
    assert 'A' not in sp_map
    assert sp_map['B'] == 2
    assert sp_map['C'] == 4
    assert sp_map['D'] == 0
    assert sp_map['E'] == 1
    assert sp_map['F'] == 7
    assert sp_map['G'] == 6

    lp_map = g.get_paths('A', longest=True)
    assert lp_map['A'] == 0
    assert lp_map['B'] == 6
    assert lp_map['C'] == 8
    assert lp_map['D'] == 3
    assert lp_map['E'] == 4
    assert lp_map['F'] == 11
    assert lp_map['G'] == 9
    
    lp_map = g.get_paths('D', longest=True)
    assert 'A' not in lp_map
    assert lp_map['B'] == 2
    assert lp_map['C'] == 5
    assert lp_map['D'] == 0
    assert lp_map['E'] == 1
    assert lp_map['F'] == 8
    assert lp_map['G'] == 6

def test_get_paths_negative():
    """
    A →(-6)→ B →(2)→ C →(3)→ F
    ↓      ↗       ↗
   (3)  (2)    (-4)
    ↓ ➚       ➚
    D →(1)→ E →(5)→ G
    """
    g = WeightedDirectedGraph()
    g.add_edges('A', {'B': -6, 'D': 3})
    g.add_edges('B', {'C': 2})
    g.add_edges('C', {'F': 3})
    g.add_edges('D', {'B': 2, 'E': 1})
    g.add_edges('E', {'C': -4, 'G': 5})
    
    sp_map = g.get_paths('A')
    assert sp_map['A'] == 0
    assert sp_map['B'] == -6
    assert sp_map['C'] == -4
    assert sp_map['D'] == 3
    assert sp_map['E'] == 4
    assert sp_map['F'] == -1
    assert sp_map['G'] == 9
    
    sp_map = g.get_paths('D')
    assert 'A' not in sp_map
    assert sp_map['B'] == 2
    assert sp_map['C'] == -3
    assert sp_map['D'] == 0
    assert sp_map['E'] == 1
    assert sp_map['F'] == 0
    assert sp_map['G'] == 6

def test_get_paths_not_dag():
    """
    A →(6)→ B 
    ↑     ↙
   (3) (2)
    ↑ ↙
    C →(1)→ D
    """
    g = WeightedDirectedGraph()
    g.add_edges('A', {'B': 6})
    g.add_edges('B', {'C': 2})
    g.add_edges('C', {'A': 3, 'D': 1})
    
    with pytest.raises(RuntimeError) as e:
        g.get_paths('A')
    
    assert 'Detected cycle.' in str(e.value)

    with pytest.raises(RuntimeError) as e:
        g.get_paths('A', longest=True)
    
    assert 'Detected cycle.' in str(e.value)

