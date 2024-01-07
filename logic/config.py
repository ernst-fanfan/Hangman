"""
This module contains the config class that will be used to
read the config file.
"""

import json

class Config:
    """
    This class will be used to read the config file.
    """
    version: str
    author: str
    
    def __init__(self, config_file):
        """
        This method will initialize the config class.
        """
        self.config_file = config_file
        self.read_config_file()
        
    def read_config_file(self):
        """
        This method will read the config file.
        """
        with open(self.config_file) as file:
            data = json.load(file)
            self.version = data["version"]
            self.author = data["author"]
            
    def get_version(self):
        """
        This method will return the version.
        """
        return self.version
    
    def get_author(self):
        """
        This method will return the author.
        """
        return self.author