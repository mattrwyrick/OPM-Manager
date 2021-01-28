

class Simulation(object):

    def __init__(self, rows):
        self.n = len(rows[0]) - 2
        self.i = 0
        self.weeks = []
        for i in range(self.n):
            week = {}
            for row in rows[1:]:
                 mid = row[0]
                 dcid = row[1]
                 key = mid+dcid
                 week[key] = int(row[i+2])
            self.weeks.append(week)

    def get_week(self):
        """
        Return the demand for each sku for the given week
        :return:
        """
        if self.season_end():
            return None
        return self.weeks[self.i]

    def go_to_next_week(self):
        """
        Go to next week
        :return:
        """
        self.i += 1
        if self.season_end():
            return -1
        return self.i

    def season_end(self):
        """
        Determine if the season has ended
        :return:
        """
        return self.i >= self.n

    def lookup_sku(self, mid, dcid):
        """
        Return
        :param mid:
        :param dcid:
        :return:
        """
        if self.season_end():
            return -1

        key = mid+dcid
        return self.weeks[self.i][key]
