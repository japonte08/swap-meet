from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self):
        original_str = super().__str__()  
        return f"{original_str} It is made from {self.fabric} fabric."
   

