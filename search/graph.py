import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # Edge case: empty graph
        if len(self.graph) == 0:
            raise ValueError(f'empty graph')
    
        # Edge case: start node not in graph
        if start not in self.graph:
            raise ValueError(f'start node not in graph')
    
        # Edge case: end node specified but not in graph
        if end is not None and end not in self.graph:
           raise ValueError(f'end not in graph')
    
        # Edge case: start equals end
        if end is not None and start == end:
            return [start]
        
        
        # initialize queue with start
        queue = deque([start])
        # initialize visited nodes
        visited = {start:None} #{node:from node}
        #initialize traversal path
        path = [start]
        #While nodes in queue, continue search
        while queue:
            # look at first node in queue
            node = queue.popleft()
            # append to list of seen nodes if not seen before
            if node not in path:
                path.append(node)
            
            # in order to get shortest_path once node is the end node (and end node is not None) 
            if end is not None and node == end:
                #initialize list for shortest_path
                shortest_path = []
                # until node == None 
                while node is not None:
                    # append to shortest path
                    shortest_path.append(node)
                    node = visited[node]
                # reverse to get path
                return shortest_path[::-1]
            
            # for current node neighbors in graph
            for neighbor in self.graph[node]:
                # if neighbor is not in visited and not in path
                if neighbor not in path and neighbor not in visited:
                    # record 
                    visited[neighbor] = node
                    queue.append(neighbor)
                    path.append(neighbor)
                    

        if end is not None:
            return None
            
        return path






