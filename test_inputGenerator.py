import unittest
import networkx as nx
import inputGenerator
import parse


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    # def test_graph_generator(self):
    #     G = nx.Graph()
    #     inputGenerator.randomGenerate(G, 10)
    #
    #     print(len(list(G.nodes)))
    #     for (u, v, wt) in G.edges.data('weight'):
    #         print("(" + str(u) + ", " + str(v) + ", " + str(wt) + ")")
    #     print("number of undirected edges in this graph is " + str(G.number_of_edges()))


    def test_30(self):

        G = inputGenerator.refine(30)

        parse.write_input_file(G, "samples_to_upload/30.in")
        H = parse.read_input_file("samples_to_upload/30.in")



    def test_50(self):
        G = inputGenerator.refine(50)

        parse.write_input_file(G, "samples_to_upload/50.in")
        H = parse.read_input_file("samples_to_upload/50.in")

    def test_100(self):

        G = inputGenerator.refine(100)

        parse.write_input_file(G, "samples_to_upload/100.in")
        H = parse.read_input_file("samples_to_upload/100.in")





if __name__ == '__main__':
    unittest.main()
