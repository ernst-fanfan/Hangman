# !/usr/bin/env python3
"""
This module contains the interface class that will be used to
run the hangman game.
"""

import tkinter as tk
from logic.config import Config

class Interface:
    """
    This class will be used to run the hangman game.
    """
    config: Config
    
    def __init__(self, config):
        """
        This method will initialize the interface class
        and draw the boot screen then present the menu.
        """
        self.config =  config
        self.draw_boot_screen()
        
        

    def draw_boot_screen(self):
        """
        This method will draw the boot screen.
        """
        self.root = tk.Tk()
        self.root.title("Hangman " + self.config.get_version())
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        self.root.mainloop()
        
    def start(self):
        """
        This method will draw the gui.
        """
        pass
    
