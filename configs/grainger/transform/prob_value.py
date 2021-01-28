import random


class ProbValue(object):

    def __init__(self, amount, value):
        """
        Creates a container for representing a probabilistic value
        :param amount: int
        :param value: any
        """
        self.amount = amount
        self.value = value

    @staticmethod
    def get_probability_list(pvs):
        """
        Create a list that represents probabilistic likelihood of choosing a value
        :param pvs: list of ProbValue
        :return: list of ProbValue.value
        """
        probability = []
        for pv in pvs:
            amount = pv.amount
            value = pv.value
            for i in range(amount):
                probability.append(value)
        random.shuffle(probability)
        return probability

    @staticmethod
    def get_value_from_probability_list(pvs, total):
        """
        Return a value from the list of probabilities
        :param pvs:
        :param total:
        :return:
        """
        if total < 1:
            return None
        n = random.randint(0, total-1)
        return pvs[n]