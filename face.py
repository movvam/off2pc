import numpy, math
from random import random

class Face():   
   
   def __init__(self, v1, v2, v3):
      self.v1 = v1
      self.v2 = v2
      self.v3 = v3
      self.area = self.calculate_area()
      self.portion = -1    # -1 means not calculated
      print(self.generate_single_point())
      #self.determine_z(v3[0],v3[1])

   def __repr__(self):
      return "\nvertices: (%s, %s, %s) area: %f"% (self.v1, self.v2, self.v3, self.area)

   def calculate_area(self):
      # ---------------------------
      #(half) cross product formula
      # ---------------------------
        
      AB = numpy.subtract(self.v2,self.v1)
      AC = numpy.subtract(self.v3,self.v1)
      
      area = 0.5 * math.sqrt(((AB[1]*AC[2]-AB[2]*AC[1])**2) + ((AB[2]*AC[0]-AB[0]*AC[2])**2) + ((AB[0]*AC[1]-AB[1]*AC[0])**2)) 
      
      return (area)
   
   def determine_z(self, x, y):
      # ---------------------------
      # given x and y, determines z on the plane
      # ---------------------------
    
      AB = numpy.subtract(self.v2,self.v1)
      AC = numpy.subtract(self.v3,self.v1)
      
      (r,s,t) = (AB[1]*AC[2]-AB[2]*AC[1]) , (AB[2]*AC[0]-AB[0]*AC[2]) , (AB[0]*AC[1]-AB[1]*AC[0])
   
      if t == 0:
         raise ValueError("cannot determine z from x and y for this plane", r, s, t)
        
      k = r*self.v1[0] + s*self.v1[1] + t*self.v1[2] 
      
      𝑧 =(1/t)*((r*self.v1[0])+(𝑠*self.v1[1])+(t*self.v1[2])-(r*x)-(s*y))

      return z
   
   def generate_single_point(self):  
        
      x_min = self.v1[0]
      x_max = self.v1[0]
      y_min = self.v1[1]
      y_max = self.v1[1]
        
      # find x_min/max and y_min/max  
      for x,y,z in (self.v1, self.v2, self.v3):
         if x > x_max:
            x_max = x
         if x < x_min:
            x_min = x
         if y > y_max:
            y_max = y
         if y < y_min:
            y_min = y
      
      scaled_x = x_min + (random() * (x_max - x_min))
      scaled_y = y_min + (random() * (y_max - y_min))
      z = self.determine_z(scaled_x, scaled_y)
        
      return (scaled_x, scaled_y, z)
    
    
         
         
      