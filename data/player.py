"""
This file contains the Player class.
"""

class Player:
    """
    This class will be used to store the player's information.
    """
    name: str
    score: int

    def __init__(self, name):
        """
        This method will initialize the player class.
        """
        self.name = name
        self.score = 0

    def get_name(self):
        """
        This method will return the player's name.
        """
        return self.name

    def set_name(self, name):
        """
        This method will set the player's name.
        """
        self.name = name

    def get_score(self):
        """
        This method will return the player's score.
        """
        return self.score

    def set_score(self, score):
        """
        This method will set the player's score.
        """
        self.score = score