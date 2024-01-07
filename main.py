# !/usr/bin/env python3
"""
This is a hangman program that will be used to learn python.
The player will be given a random word and will have to guess
the letters in the word. The player will have 6 guesses before
they lose the game. If the player guesses all the letters in
the word, they win the game.
tkinter will be the GUI for the game. The player will play against
an AI that will guess the letters in the word. The AI will have
6 guesses before it loses the game. If the AI guesses all the
letters in the word, the player loses the game.

Main.py will be the main file that will run the game.
"""

from gui.interface import Interface
from logic.config import Config

if __name__ == "__main__":
    config = Config("config.json")
    interface = Interface(config=config)