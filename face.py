class Face():   
   
   def __init__(self, v1, v2, v3):
      self.v1 = v1
      self.v2 = v2
      self.v3 = v3
      #self.area = calculate_area()

   def __repr__(self):
      return "\nvertices: (%d, %d, %d)"% (self.v1, self.v2, self.v3)

   #def calculate_area():
      
