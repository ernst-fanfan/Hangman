# !/usr/bin/env python3
"""
This module contains the interface class that will be used to
run the hangman game.
"""

import tkinter as tk
from logic.config import Config
from logic.state import State

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
        self.state = State()
        self.draw_boot_screen()
        
        

    def draw_boot_screen(self):
        """
        This method will draw the boot screen.
        """
        self.root = tk.Tk()
        self.root.title("Hangman " + self.config.get_version())
        self.root.geometry("800x600")
        self.root.resizable(False, False)
        intro = tk.Label(
            self.root, text=self.state.get_message(), font=("Arial", 20),
            justify=tk.CENTER, wraplength=600
            )
        intro.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.root.mainloop()
        
    def start(self):
        """
        This method will draw the gui.
        """
        pass
    
