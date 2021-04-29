import unittest

import networkx

import solver
import parse
import utils
import networkx as nx


class MyTestCase(unittest.TestCase):
    def test_solver(self):
        path = "samples/30.in"
        G = parse.read_input_file(path)
        # allWeights = nx.get_edge_attributes(G, "weight")
        # print(allWeights[(0, 11)]+allWeights[(11,26)]+allWeights[(26,29)])
        c, k = solver.solve(G)
        assert utils.is_valid_solution(G, c, k)
        print("Shortest Path Difference: {}".format(utils.calculate_score(G, c, k)))
        parse.write_output_file(G, c, k, 'TESTING_SOLVER/given_sample_30.out')

    def test_networkx(self):
        G = networkx.Graph()
        G.add_edge(0, 1, weight=3)
        print(nx.shortest_path_length(G, 0, 1, weight="weight"))

    def test_sample_out(self):
        c = [1]
        k = [(0, 27),(24,29),(26,29),(20,16)]
        path = "samples/30.in"
        G = parse.read_input_file(path)
        print(utils.calculate_score(G, c, k))

if __name__ == '__main__':
    unittest.main()
