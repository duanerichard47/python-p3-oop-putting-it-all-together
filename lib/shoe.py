#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, color, size, material, condition):
        self.brand = brand
        self.color = color
        self.size = size
        self.material = material
        self.condition = condition


    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) != int:
            print("page_count must be an integer")
        else:
         self._page_count = page_count

    page_count = property(get_page_count, set_page_count)







































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
      