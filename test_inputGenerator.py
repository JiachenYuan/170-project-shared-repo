import unittest
import networkx as nx
import inputGenerator



class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_graph_generator(self):
        G = nx.Graph()
        numVertices = inputGenerator.randomGenerate(G, 10)
        print(str(numVertices))
        for (u, v, wt) in G.edges.data('weight'):
            print("("+str(u)+", "+str(v)+", "+str(wt)+")")

if __name__ == '__main__':
    unittest.main()
