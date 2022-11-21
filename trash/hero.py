class hero:
    def __init__(self,name,level=1, cls= "ranger"):
        self.level = level
        self.cls = cls
        self.name = name
        if cls == "ranger":
            self.int = 8
            self.str = 8
            self.dex = 14
        def equip(self,id):
            self.helmet = id