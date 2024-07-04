import math

class Vector:
    def __init__(self,vector1x,vector1y,vector2x,vector2y):
        # Making them local variables
        self.vector1x = vector1x
        self.vector1y = vector1y
        self.vector2x = vector2x
        self.vector2y = vector2y
        #doing the addition to find the total vector
        self.final_vector_y = self.vector1y + self.vector2y
        self.final_vector_x = self.vector1x + self.vector2x
    def __str__(self):
        #returning the final vector in a legible format
        return f'Your final vector would be ({self.final_vector_x}: {self.final_vector_y})'
    
    def __repr__(self):
        #returning each vector in an illegible format
        return f"Vector1({self.vector1x}:{self.vector1y}), Vector2({self.vector2x}, {self.vector2y})"
    
     def __add__(self, other):
         #check to make sure the other is a vector too
         if isinstance(other, Vector):
             # Perform vector addition
             new_vector_x = self.vector1x + other.vector2x
             new_vector_y = self.vector1y + other.vector2y
             return Vector(new_vector_x, new_vector_y)
         else:
             #throws an error message if other isn't a vector
             raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other))) 
     
     def __len__(self):
         #Calculates the length of each vector
         length_vector1 = math.sqrt(self.vector1x**2 + self.vector1y**2)
         length_vector2 = math.sqrt(self.vector2x**2 + self.vector2y**2)
         #returns the length of each vector
         return length_vector1 + length_vector2



    


    