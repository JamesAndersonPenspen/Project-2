import math

class Vector:
    def __init__(self,vector1x,vector1y,vector2x,vector2y):
        self.vector1x = vector1x
        self.vector1y = vector1y
        self.vector2x = vector2x
        self.vector2y = vector2y
        self.final_vector_y = self.vector1y + self.vector2y
        self.final_vector_x = self.vector1x + self.vector2x
    def __str__(self):
        return f'Your final vector would be ({self.final_vector_x}: {self.final_vector_y})'
    
    def __repr__(self):
        return f"Vector1({self.vector1x}:{self.vector1y}), Vector2({self.vector2x}, {self.vector2y})"
    
     def __add__(self, other):
         if isinstance(other, Vector):
             # Perform vector addition
             new_vector_x = self.vector1x + other.vector2x
             new_vector_y = self.vector1y + other.vector2y
             return Vector(new_vector_x, new_vector_y)
         else:
             raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other))) 
     
     def __len__(self):
         length_vector1 = math.sqrt(self.vector1x**2 + self.vector1y**2)
         length_vector2 = math.sqrt(self.vector2x**2 + self.vector2y**2)
         return length_vector1 + length_vector2



    


    