import networkx as nx
from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_score
import sys
from os.path import basename, normpath
import glob

import random


def solve(G):
    """
    Args:
        G: networkx.Graph
    Returns:
        c: list of cities to remove
        k: list of edges to remove
    """
    H = G.copy()
    num_of_nodes = len(H.nodes())
    c, k = setBudgets(num_of_nodes)
    nodesDeleted = []
    edgesDeleted = []

    while c != 0 or k != 0:
        currShortestPath = nx.shortest_path(H, 0, num_of_nodes - 1,'weight')
        currShortestPathLength = nx.shortest_path_length(H, 0, num_of_nodes-1, 'weight')

        edgesAlongShortestPath = []
        nodesAlongShortestPath = []
        for i in range(1, len(currShortestPath)):
            edgesAlongShortestPath.append((currShortestPath[i - 1], currShortestPath[i]))
            if i != (len(currShortestPath) - 1):
                nodesAlongShortestPath.append(currShortestPath[i])

        bool_willDeleteANode = False
        bool_willDeleteAnEdge = False
        node_yielding_max_length = None
        edge_yielding_max_length = None

        if k == 0 and c == 0:  # redundant...
            return nodesDeleted, edgesDeleted
        elif k == 0 and c != 0:
            bool_willDeleteANode = True
            node_yielding_max_length, max_length = nodeToDelete(currShortestPathLength, H, num_of_nodes, nodesAlongShortestPath)
        elif k != 0 and c == 0:
            bool_willDeleteAnEdge = True
            edge_yielding_max_length, max_length = edgeToDelete(currShortestPathLength, H, num_of_nodes, edgesAlongShortestPath)
        else:
            node_yielding_max_length, max_length_node = nodeToDelete(currShortestPathLength, H, num_of_nodes, nodesAlongShortestPath)
            edge_yielding_max_length, max_length_edge = edgeToDelete(currShortestPathLength, H, num_of_nodes, edgesAlongShortestPath)
            if max_length_edge >= max_length_node:
                bool_willDeleteAnEdge = True
            else:
                bool_willDeleteANode = True

        if bool_willDeleteANode and (node_yielding_max_length is None):
            return nodesDeleted, edgesDeleted
        elif bool_willDeleteAnEdge and (edge_yielding_max_length is None):
            return nodesDeleted, edgesDeleted
        else:
            if bool_willDeleteANode and (not bool_willDeleteAnEdge):
                nodesDeleted.append(node_yielding_max_length)
                H.remove_node(node_yielding_max_length)
                c = c - 1  # budget for nodes is decreased by 1
            if bool_willDeleteAnEdge and (not bool_willDeleteANode):
                edgesDeleted.append(edge_yielding_max_length)
                H.remove_edge(edge_yielding_max_length[0], edge_yielding_max_length[1])
                k = k - 1  # budget for edges is decreased by 1
    return nodesDeleted, edgesDeleted


# helper functions:
def setBudgets(num_of_nodes):
    if num_of_nodes <= 30:
        return 1, 15
    elif num_of_nodes <= 50:
        return 3, 50
    elif num_of_nodes <= 100:
        return 5, 100


def IsTuple(x):
    return type(x) is tuple


def IsDrawFromEdges():
    return random.uniform(0, 1) <= 0.5


def nodeToDelete(curr_max_length, H, num_of_nodes, nodesAlongShortestPath):
    max_length = curr_max_length
    node_yielding_max_length = None

    for v in nodesAlongShortestPath:
        H_temp = H.copy()
        H_temp.remove_node(v)
        if nx.is_connected(H_temp):
            updated_shortest_path_length = nx.shortest_path_length(H_temp, 0, num_of_nodes - 1, weight="weight")
            if updated_shortest_path_length >= max_length:
                max_length = updated_shortest_path_length
                node_yielding_max_length = v
    return node_yielding_max_length, max_length


def edgeToDelete(curr_max_length, H, num_of_nodes, edgesAlongShortestPath):
    max_length = curr_max_length
    edge_yielding_max_length = None
    for u, v in edgesAlongShortestPath:
        H_temp = H.copy()
        H_temp.remove_edge(u, v)
        if nx.is_connected(H_temp):
            updated_shortest_path_length = nx.shortest_path_length(H_temp, 0, num_of_nodes - 1, weight="weight")
            if updated_shortest_path_length >= max_length:
                max_length = updated_shortest_path_length
                edge_yielding_max_length = (u, v)
    return edge_yielding_max_length, max_length


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G = read_input_file(path)
    c, k = solve(G)
    assert is_valid_solution(G, c, k)
    print("Shortest Path Difference: {}".format(calculate_score(G, c, k)))
    write_output_file(G, c, k, 'TESTING_SOLVER/given_sample_30.out')

# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
#if __name__ == '__main__':
#    inputs = glob.glob('inputs/large/*')
#    for input_path in inputs:
#        output_path = 'outputs/large/' + basename(normpath(input_path))[:-3] + '.out'
#        G = read_input_file(input_path)
#        c, k = solve(G)
#        assert is_valid_solution(G, c, k)
#        distance = calculate_score(G, c, k)
#        write_output_file(G, c, k, output_path)
