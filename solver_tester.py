import unittest
import solver
import parse
import utils
import networkx as nx


class MyTestCase(unittest.TestCase):
    def test_solver(self):
        path = "samples/30.in"
        G = parse.read_input_file(path)
        allWeights = nx.get_edge_attributes(G, "weight")
        print(allWeights[(0, 11)]+allWeights[(11,26)]+allWeights[(26,29)])
        c, k = solver.solve(G)
        assert utils.is_valid_solution(G, c, k)
        print("Shortest Path Difference: {}".format(utils.calculate_score(G, c, k)))

if __name__ == '__main__':
    unittest.main()
