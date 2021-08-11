from __future__ import annotations
import random

# Node O(1) add, O(1) neighbor exists, O(n) neighbor search by value
class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.neighbors = []
        self.neighbors_set = set()

    def add_neighbor(self,  node: Node):
        if not isinstance(node, Node):
            raise Exception("Type should be of Node.")

        if node not in self.neighbors_set:
            self.neighbors.append(node)
            self.neighbors_set.add(node)

    def exists_in_neighbors(self, node: Node):
        if not isinstance(node, Node):
            return False
        return node in self.neighbors_set

    def get_random_neighbor(self):
        if self.neighbors is not None:
            random_neighbor_index = random.randint(0, len(self.neighbors))
            return self.neighbors[random_neighbor_index]
        return None

    def get_neighbor(self, neighbor_val):
        for node in self.neighbors:
            if node.val == neighbor_val:
                return node
        return None

    # computationally expensive
    def not_neighbors(self, node_list):
        node_set = set(node_list)
        return list(node_set - self.neighbors_set) + list(self.neighbors_set - node_set)

    def __str__(self):
        out = "Value: " + str(self.val) + "\n"
        out += "Neighbors: ["
        for i in self.neighbors:
            out += str(i.val)
            out += ", "
        out = out.strip(", ")
        out += "]"
        return out

