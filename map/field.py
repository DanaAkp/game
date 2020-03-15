from dataclasses import dataclass
#from base.unit import Units
#from base.ground import Ground
#from image import Image


@dataclass
class Field:
    list_unit: list
    list_ground: list

    def is_can_move_unit(self, x, y):
        for un in self.list_unit:
            if un.x==x and un.y==y:
                return False
        for gr in self.list_ground:
            if not gr.can_move_unit:
                if gr.x==x and gr.y==y:
                    return False
        return True

    
    



