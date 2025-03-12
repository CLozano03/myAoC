from typing import List, Dict, Set
from collections import defaultdict

FILENAME = "input.txt"


# Implementing the Bron-Kerbosch algorithm myself so I can understand it better and I dont feel like I'm cheating
def bron_kerbosch(connections: Dict[str, List[str]]) -> List[Set[str]]:
    def bron_kerbosch_rec(
        R: Set[str], P: Set[str], X: Set[str], cliques: List[Set[str]]
    ):
        """
        R (Set[str]): Current clique
        P (Set[str]): Nodes that can be added to the clique
        X (Set[str]): Nodes that can't be added to the clique
        """

        if not P and not X:  # If P and X are empty, we have a clique
            cliques.append(R)
            return

        for node in list(P):
            neighbors = set(connections.get(node, []))
            bron_kerbosch_rec(
                R | {node}, P & neighbors, X & neighbors, cliques
            )
            P.remove(node)  # Remove the node from P
            X.add(node)  # Add the node to X so we don't visit it again

    cliques = []
    nodes = set(connections.keys())
    bron_kerbosch_rec(
        set(), nodes, set(), cliques
    )  # Start finding cliques with an empty R
    return cliques


# -------------------------------------------------------------------------------
connections: Dict[str, List[str]] = defaultdict(list)

for line in open(FILENAME):
    k, v = line.strip().split("-")
    connections[k].append(v)
    connections[v].append(k)

res = ",".join(sorted(max(bron_kerbosch(connections), key=len)))
print(f"Maximum clique: {res}")
