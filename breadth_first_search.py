def bfs(graph, start):
    """
    Performs breadth-first search on the given graph.

    Parameters:
        graph (dict): a dictionary where the keys are vertices and the values are lists of connected vertices
        start (int): the starting vertex

    Returns:
        set: a set of all the vertices that were visited
    """
    # Create a queue and add the starting node to it
    queue = deque(graph[start])
    # Create a set to keep track of the visited nodes
    searched = set([start])
    
    # Loop until there are no more nodes in the queue
    while queue:
        # Get the next node from the queue
        vertex = queue.popleft()
        # If the node has not been visited, add all its neighbors to the queue
        if not vertex in searched:
            queue += graph[vertex]
            # Add the node to the set of visited nodes
            searched.add(vertex)
    
    # Return a set of all the visited nodes
    return searched

import unittest
from collections import deque
from breadth_first_search import bfs

class TestBFS(unittest.TestCase):
    def test_empty_graph(self):
        graph = {}
        start = None
        with self.assertRaises(KeyError):
            bfs(graph, start)

    def test_single_vertex_graph(self):
        graph = {1: []}
        start = 1
        self.assertEqual(bfs(graph, start), {1})

    def test_multiple_vertices_graph(self):
        graph = {1: [2, 3], 2: [4], 3: [4], 4: []}
        start = 1
        self.assertEqual(bfs(graph, start), {1, 2, 3, 4})

    def test_disconnected_vertices_graph(self):
        graph = {1: [], 2: [3], 3: []}
        start = 1
        self.assertEqual(bfs(graph, start), {1})

    def test_graph_with_cycle(self):
        graph = {1: [2], 2: [3], 3: [1]}
        start = 1
        self.assertEqual(bfs(graph, start), {1, 2, 3})

    def test_invalid_input_graph(self):
        graph = "not a dictionary"
        start = 1
        with self.assertRaises(TypeError):
            bfs(graph, start)

    def test_invalid_input_start_vertex(self):
        graph = {1: [2], 2: []}
        start = 3
        with self.assertRaises(KeyError):
            bfs(graph, start)

if __name__ == '__main__':
    unittest.main()