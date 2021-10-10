#!/usr/bin/python3



class Resources:
    """
    Implements addResource to add the resources.
    """

    def __init__(self):
    
        self.resources = {}

    def addResource(self, resource, parents=[]):
       
        self.resources.setdefault(resource, set())
        self.resources[resource].update(parents)
