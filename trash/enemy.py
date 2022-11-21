class enemy:
    def __init__(self,name,level=1, mod= "ranger"):
        self.level = level
        self.mod = mod
        self.name = name
        def equip(self,id):
            self.helmet = id