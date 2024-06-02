from Node import Node
import random

class Graph:

    @staticmethod
    def generate_random_undirected(size):

        # node list for generating random cycles
        node_list = []

        # initial node
        root_node = Node(0)
        node_list.append(root_node)
        the_node = root_node

        # generate i new nodes and perform operations on them
        for i in range(1, size):
            new_node = Node(i)
            node_list.append(new_node)

            # make nodes neighbors (undirected so both are neighbors)
            new_node.add_neighbor(the_node)
            the_node.add_neighbor(new_node)

            # generate cycle 30% chance
            if random.randint(0, 100) < 30:
                not_neighbors = the_node.not_neighbors(node_list)
                if len(not_neighbors) > 0:
                    cycle_index = random.randint(0, len(not_neighbors) - 1 )
                    the_node.add_neighbor(not_neighbors[cycle_index])

            # progress to next node in graph 30% chance
            if random.randint(0, 100) < 30:
                the_node = new_node

        return root_node

    def bfs_print(start_node):
        queue = []
        visited = set()

        # initialize
        queue.append(start_node)

        while len(queue) > 0:
            node = queue.pop(0)
            print(node)

            for neighbor in node.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(node)



