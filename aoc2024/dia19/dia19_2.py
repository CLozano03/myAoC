from typing import List
from functools import lru_cache

FILENAME = "input.txt"


class TreeNode:
    def __init__(self, value: str):
        self.value: str = value
        self.children = {}

    def __repr__(self):
        return f"TreeNode({self.value})"


class Tree:
    """
    This class acts as an aplhabet of towels
    """

    def __init__(self):
        self.root = TreeNode(
            "~"
        )  # Root node. This char is not part of the alphabet

    def add_towel(self, towel: str):
        current_node: TreeNode = self.root

        for c in towel:
            if c not in current_node.children:
                current_node.children[c] = TreeNode(c)
            current_node = current_node.children[c]

        current_node.children["$"] = TreeNode(
            "$"
        )  # '$' Means end of the towel

    def search_all_coincidences(self, string: str) -> List[str]:
        """
        Looks for all the coincidences of the string in the tree
        """
        stream: str = ""
        curr_node: TreeNode = self.root
        string_it = 0
        coincidences: List[str] = []

        while string_it < len(string):
            c = string[string_it]

            if c in curr_node.children:
                stream += c
            else:
                break

            curr_node = curr_node.children[c]

            if "$" in curr_node.children:
                coincidences.append(stream)

            string_it += 1

        return coincidences


# -------------------------------------------------------------------------------
@lru_cache(maxsize=None)
def ways_make_design(design: str) -> int:
    """
    Returns number of ways in which design can be printed on the towel (Recursive)
    """
    coincidences: List[str] = towel_alphabet.search_all_coincidences(design)
    ret: int = 0

    for coincidence in coincidences:
        if len(coincidence) == len(design):
            ret += 1
            continue
        ret += ways_make_design(design[len(coincidence) :])

    return ret


# -------------------------------------------------------------------------------
towels_str, des_designs = open(FILENAME).read().split("\n\n")
towels: List[str] = towels_str.split(", ")
desired_designs: List[str] = des_designs.split("\n")

towel_alphabet: Tree = Tree()
for towel in towels:
    towel_alphabet.add_towel(towel)

possible_designs = sum(ways_make_design(design) for design in desired_designs)
print(f"Possible designs: {possible_designs}")
