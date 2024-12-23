import networkx as nx # pip install networkx

FILENAME = "input.txt"

G = nx.Graph() # All computers represent nodes, and connections represent edges

for line in open(FILENAME):
    node, neighbor = line.strip().split("-")
    G.add_edge(node, neighbor)

# Find all cliques: nodes that are all interconnected between them
cliques = list(nx.find_cliques(G))

res = ",".join(sorted(max(cliques, key=len)))
print(f'Maximum clique: {res}')