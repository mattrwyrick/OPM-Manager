
from copy import deepcopy

from opm_manager.models.sku import DistributionCenter
from opm_manager.models.supplier import Supplier


class Node(object):

    def __init__(self, location, weight):
        """
        Represents a distribution center or supplier in the supply chain network
        :param location: DistributionCenter or Supplier
        :param weight: float [0, 1]
        """
        self.location = location
        self.is_dc = type(location) == DistributionCenter
        self.weight = weight
        self.neighbors = []
        self.individual_score = 0
        self.relative_score = 0

    @property
    def neighbors_magnitude(self):
        """
        Get the neighbor weight magnitude
        :return:
        """
        return sum((n.weight for n in self.neighbors))

    def __deepcopy__(self, memodict={}):
        """
        Deep clone of a Node
        :return:
        """
        return Node(deepcopy(self.location), self.weight)


class Network(object):

    def __init__(self, dcs, suppliers, neighbor_threshold):
        """
        Represents a supply chain
        :param dcs:
        :param suppliers:
        :param neighbor_threshold:
        """

        nodes = []
        locations = dcs + suppliers
        total_space = sum([dc.max_cube for dc in dcs])
        for loc in locations:
            weight = 0
            if type(loc) == DistributionCenter:
                weight = loc.max_cube / total_space
            node = Node(loc, weight)
            nodes.append(node)

        for node1 in nodes:
            for node2 in nodes:
                if node1 != node2:
                    if type(node1.location) == Supplier and type(node2.location) == DistributionCenter:
                        node1.neighbors.append(node2)
                    elif type(node1.location) == DistributionCenter and type(node2.location) == Supplier:
                        node1.neighbors.append(node2)
                    elif type(node1.location) == DistributionCenter and type(node2.location) == DistributionCenter:
                        if node1.location.distance(node2.location) < neighbor_threshold:
                            node1.neighbors.append(node2)

        self.nodes = {n.location.id: n for n in nodes}

    def get_network_score(self):
        """
        Update the scores in within the network and calculate the network score (relative)
        :return:
        """
        for key in self.nodes:
            node = self.nodes[key]
            if node.is_dc:
                neighbors_total = 0
                for neighbor in node.neighbors:
                    weight = (neighbor.weight / node.neighbors_magnitude)
                    neighbors_total += weight * neighbor.individual_score

                neighbor_score = neighbors_total / len(node.neighbors)
                relative_score = (node.individual_score + neighbor_score) / 2
                node.relative_score = relative_score

        total = 0
        for key in self.nodes:
            node = self.nodes[key]
            total += node.relative_score
        score = total / len(self.nodes)

        return score

    def __deepcopy__(self, memodict={}):
        """
        Deep copy of the Network
        :return:
        """
        nodes = [deepcopy(n) for n in self.nodes]
        return Network(nodes)

