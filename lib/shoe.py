#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size=0):
        self.brand = brand
        self.size = size
     

    def get_size(self):
        return self._size
    
    def set_size(self, size):
        if type(size) != int:
            print("size must be an integer")
        else:
         self._size = size

    size = property(get_size, set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"




# class Shoe:
#     def __init__ (self, brand):
#       self.brand = brand
#       self.color = None
#       self.size = None
#       self.condition = None

#     def set_size(self, new_size):
#        if type(new_size) != int:
#           print('idk')
#        else:
#           self._size = new_size
      
#     def get_size(self):
       
#     size = property(get_size, set_size)

#     def cobble(self):
#        self.condition
      