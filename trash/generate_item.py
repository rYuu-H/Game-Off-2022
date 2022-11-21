import math
from random import randint
import string 


class item:
    def __init__(self, ilvl, part):
        self.create(ilvl, part)

    def create(self, ilvl, part):
        self.part = part
        self.ilvl = ilvl
        if part == "":
            part = randint(1, 10)
        print("created " , ilvl, part )



a = item(55,"weapon")
