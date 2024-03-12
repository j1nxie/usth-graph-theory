import networkx as nx
from networkx import Graph


def find_cliques_n(graph: Graph, n: int) -> list:
    cliques = []
    for clique in nx.find_cliques(graph):
        if len(clique) == n:
            cliques.append(clique)

    return cliques


G = nx.random_graphs.random_regular_graph(3, 30, seed=42)

result = find_cliques_n(G, 2)
print(result)
