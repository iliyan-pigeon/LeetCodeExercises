# Solution 1
import random


class RandomizedSet(object):

    def __init__(self):
        self.set = []

    def insert(self, val):
        if val not in self.set:
            self.set.append(val)
            return True

        return False

    def remove(self, val):
        if val in self.set:
            self.set.remove(val)
            return True

        return False

    def getRandom(self):
        
        return random.choice(self.set)


# Solution 2
import random


class RandomizedSet:
    def __init__(self):
        self.dict = {}  
        self.list = [] 

    def insert(self, val):
        if val in self.dict:
            return False  
        self.dict[val] = len(self.list)  
        self.list.append(val)  
        return True

    def remove(self, val):
        if val not in self.dict:
            return False  
        
        index_to_remove = self.dict[val]
        last_element = self.list[-1] 

        
        self.list[index_to_remove] = last_element
        self.dict[last_element] = index_to_remove

        
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self):
        return random.choice(self.list)
