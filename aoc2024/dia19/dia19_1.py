from typing import List

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
def design_possible(design: str) -> bool:
    """
    Returns True if the design can be printed on the towel (Recursive)
    """
    coincidences: List[str] = towel_alphabet.search_all_coincidences(design)

    for coincidence in coincidences:
        if design.startswith(coincidence):
            if len(coincidence) == len(design):
                return True
            else:
                ret: bool = design_possible(design[len(coincidence) :])
                if ret:
                    return True
        else:
            raise Exception("This should not happen")

    return False  # If no coincidence is found, the design is not possible


# -------------------------------------------------------------------------------
towels_str, des_designs = open(FILENAME).read().split("\n\n")
towels: List[str] = towels_str.split(", ")
desired_designs: List[str] = des_designs.split("\n")

towel_alphabet: Tree = Tree()
for towel in towels:
    towel_alphabet.add_towel(towel)

possible_designs = sum(
    1 for design in desired_designs if design_possible(design)
)
print(f"Possible designs: {possible_designs}")
