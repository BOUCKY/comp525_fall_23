"""
Parser for Ramen Stats
Jon
20211210
"""


class RamenStats:
    """
    Ramen stats provide interface for reading and parsing ramen stats
    """

    file_name = 'ramen.csv'

    def __init__(self):
        """
        Constructor
        """
        self.ramen_set = []
        with open(self.file_name, 'r', encoding='UTF-8') as fin:
            lines = fin.readlines()[1:]
            # Do something with the lines in order to fill self.ramen_set
            # with useful data
            for line in lines:
                line = line.strip()
                line = line.split(',')
                line[5] = float(line[5])
                self.ramen_set.append(line)
        # print(self.ramen_set)


    def get_average_for_all(self):
        """
        Returns the average ramen rating across ALL ratings
        :return: the average for ratings for the given country
        :rtype: float
        """
        total_rating = 0
        for ramen in self.ramen_set:
            total_rating += ramen[5]
        return total_rating / len(self.ramen_set)

    def get_average_for_country(self, country):
        """
        Returns the average ramen rating for a given country
        :param country: the country for which the ratings belong to
        :type country: string
        :return: the average for ratings for the given country
        :rtype: float
        """
        total_rating = 0
        country_ratings = 0
        for ramen in self.ramen_set:
            if ramen[4] == country:
                country_ratings += 1
                total_rating += ramen[5]
        return total_rating / country_ratings

    def get_percent_of_variety_that_include_the_word_ramen(self):
        """
        Returns the percentage of ramen variety that include the word "ramen"
        :return: the percentage of ramen variety that include the word "ramen"
        :rtype: float
        """
        country_ratings = 0
        for ramen in self.ramen_set:
            if 'Ramen' in ramen[2]:
                country_ratings += 1
        return country_ratings / len(self.ramen_set)

    def get_ramen_by_country(self):
        """
        Returns a dictionary with the ramen categorized by country
        :return:  dict with keys being the country name and values being
            a list of ramen for that country
            ex: {'USA': [[2580, 'New Touch', "T's Restaurant', 'Cup', 'etc]]
        :rtype: dictionary
        """
        data = {}
        for ramen in self.ramen_set:
            country = ramen[4]
            if country not in data:
                data[country] = []
            data[country].append(ramen)
        return data


if __name__ == "__main__":
    stats = RamenStats()

    # # average all expected to be ???
    print(f"Average All: {stats.get_average_for_all():.2f}")

    # # average USA expected to be ???
    print(f"Average USA: {stats.get_average_for_country('USA'):.2f}")

    # # Num ramen with "ramen" in their variety expected to be ???
    percent_ramen = stats.get_percent_of_variety_that_include_the_word_ramen()
    print(f"Variety % ramen: {percent_ramen:.2f}")

    # # Num ramen for Japan expected to be ???
    ramen_categorized = stats.get_ramen_by_country()
    print(f"Num ramen for Japan: {len(ramen_categorized['Japan'])}")
