"""
practice_dictionaries.py
Get familiar with dictionaries
Mihaela Sabin
Created March 20, 2019
Updated October 16, 2019; February 19, 2020
"""


class Practice(object):
    """
    Illustrate methods that transform an input dictionary into some output
    """

    def parse_seasons(self, season_dict):
        """
        Create a string with info from season_dict
        season_dict: dictionary
            keys: strings - season names
            values: strings - season descriptions
        Returns: string with season names and descriptions and no spaces or
            other characters in between
        """
        result = ""
        for season, description in season_dict.items():
            result += f"{season}{description}"
        return result.strip()

    def update_inventory(self, inventory_dict, quantity_added):
        """
        Returns new dictionary with quanties for each itmem in inveentory_dict
            increased by quantity-added
        inventory_dict: dictionary
            keys: strings - inventory item names
            values: int - inventory quantity of item
        Returns: dictionry
        """
        updated_inventory = {}
        for item, quantity in inventory_dict.items():
            updated_inventory[item] = quantity + quantity_added
        return updated_inventory

if __name__ == '__main__':
    p = Practice()
    input1 = {
        'spring': 'warm',
        'summer': 'hot',
        'fall': 'just right',
        'winter': 'cold'
    }
    result = p.parse_seasons(input1)
    print(f'parse_seasons({input1}) returns {result}')