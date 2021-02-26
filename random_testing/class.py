from defclass import new
#this is the class:
'''
class new:
    def __init__(self, name, size, age, is_dead): these are the values that are
                being passed in self(aka whatever object is being created/referenced)
                they are then stored as attributes in that object (self.whatever)
        self.name = name 
        self.size = size
        self.age = age
        self.is_dead = is_dead 

'''

obj1 = new("john", "large", 12, True)
print(obj1.old_person()) #self.name for this specific object
print()





