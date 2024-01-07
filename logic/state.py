"""
This module contains the state class that will be used to
store the state of the game.
"""

from data.player import Player

class State:
    """
    This class will be used to store the state of the game.
    """
    message: str
    word: str
    mask: str
    game_over: bool
    players: list[Player]
    
    def __init__(self):
        """
        This method will initialize the state class.
        """
        self.message = "Welcome to Hangman!"
        self.word = ""
        self.mask = ""
        self.game_over = False
        self.win = False
        self.lose = False
        self.players = []
        
    def get_message(self):
        """
        This method will return the message.
        """
        return self.message
    
    def set_message(self, message):
        """
        This method will set the message.
        """
        self.message = message
        
    def get_word(self):
        """
        This method will return the word.
        """
        return self.word
    
    def set_word(self, word):
        """
        This method will set the word.
        """
        self.word = word
    
    def get_mask(self):
        """
        This method will return the mask.
        """
        return self.mask
    
    def set_mask(self, mask):
        """
        This method will set the mask.
        """
        self.mask = mask
        
    def get_game_over(self):
        """
        This method will return the game over.
        """
        return self.game_over
    
    def set_game_over(self, game_over):
        """
        This method will set the game over.
        """
        self.game_over = game_over
