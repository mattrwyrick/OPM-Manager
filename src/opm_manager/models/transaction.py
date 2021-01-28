

class Transaction(object):

    HEADER = ["Material", "Source", "Destination", "Cube", "Time"]

    def __init__(self, material, src, tgt, cube, duration):
        """
        Represents a material transaction in the supply chain network
        :param material:
        :param src:
        :param tgt:
        :param cube:
        :param duration:
        """
        self.material = material.id
        self.source = src.id
        self.target = tgt.id
        self.cube = cube
        self.duration = duration

    def as_row(self):
        """
        Return the object as a list
        :return: list
        """
        return [self.material, self.source, self.target, self.cube, self.duration]
