import networkx as nx
import parse
import random

G = nx.Graph()


def randomGenerate(g, numVertices):
    # add 1<=|V|<=numVertices number of vertices to the graph G. |V| is randomly picked in the range.
    lst = list(range(1, numVertices))
    randomNum = random.choice(lst)
    g.add_nodes_from(list(range(randomNum)))

    # add edges to the graph G randomly, edge weight is between 0 and 100 (exclusively).
    vertices = list(range(randomNum))
    edgeChecker = [[False for j in range(len(vertices))] for i in range(len(vertices))]
    for i in range(len(edgeChecker)):
        for j in range(len(edgeChecker[0])):
            if i == j:
                edgeChecker[i][j] = -1

    for i in range(len(edgeChecker)):
        for j in range(len(edgeChecker[0])):
            if edgeChecker[i][j] == False and edgeChecker != -1:
                probToAdd = random.uniform(0, 1)
                if probToAdd > 0.5:
                    decimalPlaceToRound = random.choice([0, 1, 2, 3])
                    weight = round(random.uniform(1, 99), decimalPlaceToRound)
                    edgeChecker[i][j] = weight
                    edgeChecker[j][i] = weight
                else:
                    edgeChecker[i][j] = 0
                    edgeChecker[j][i] = 0

    for i in range(len(edgeChecker)):
        for j in range(len(edgeChecker[0])):
            if edgeChecker[i][j] >= 1:
                g.add_edge(i, j, weight=edgeChecker[i][j])
    return randomNum

""" 2 limitations to satisfy: 
                    1. every vertex should have degree at least 2
                    2. the graph generated is connected. Maybe use DFS to check this property...
                    3. number of vertices are sufficiently large, measured by some threshold----
                                                                                    small graphs: 20-30
                                                                                    medium graphs: 31-50
                                                                                    large graphs: 51-100
                                                                                        ~ from Piazza
"""

def refine(num):
    # check limitation 3
    G = nx.Graph()
    if num == 30:
        randomGenerate(G, 30)
        if G.number_of_nodes() < 20 or G.number_of_nodes() > 30:
            return refine(30)
    if num == 50:
        randomGenerate(G, 50)
        if G.number_of_nodes() < 31 or G.number_of_nodes() > 50:
            return refine(50)
    if num == 100:
        randomGenerate(G, 100)
        if G.number_of_nodes() < 51 or G.number_of_nodes() > 100:
            return refine(100)

    # check limitation 2
    # Idea: a graph is only connected iff |E| >= |V|-1
    if G.number_of_edges() < G.number_of_nodes() - 1:
        return refine(num)


    # check limitation 1
    v_d_pair = list(G.degree(list(range(G.number_of_nodes()))))
    for v, d in v_d_pair:
        if d < 2:
            return refine(num)

    return G



