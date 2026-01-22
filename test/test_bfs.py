# write tests for bfs
import pytest
from search.graph import (Graph)


def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    # Load the graph
    test_graph = Graph('data/tiny_network.adjlist') 
    
    # Run BFS traversal
    start_node = list(test_graph.graph.keys())[0]
    result = test_graph.bfs(start_node)
    
    # Assert first node is start node
    assert result[0] == start_node
    
    # Assert all nodes are traversed
    assert len(result) == len(test_graph.graph)
    
    # Test edge case: empty graph raises ValueError
    empty_graph = Graph()
    empty_graph.graph = {}
    with pytest.raises(ValueError):
        empty_graph.bfs('A')
    
    # Test edge case: start node not in graph raises ValueError
    with pytest.raises(ValueError):
        test_graph.bfs('random_node')
    

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
   # Load the graph
    test_graph = Graph('data/citation_network.adjlist')  
    
    # Get two nodes
    nodes = list(test_graph.graph.keys())
    start = nodes[0]
    end = nodes[5]
    
    # Run BFS 
    result = test_graph.bfs(start, end)
    
    # If path exists, check validity
    if result is not None:
        # Assert path starts with start node
        assert result[0] == start
        
        # Assert path ends with end node
        assert result[-1] == end
        
        # Assert path is connected (each node connects to next)
        for i in range(len(result) - 1):
            assert result[i + 1] in test_graph.graph[result[i]]
    
    # Test disconnected nodes return None
    disconnected_graph = Graph()
    disconnected_graph.graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C']
    }
    result_none = disconnected_graph.bfs('A', 'C')
    assert result_none is None
    
    # Test edge case: end node not in graph raises ValueError
    with pytest.raises(ValueError):
        test_graph.bfs(start, 'nonexistent_node')
