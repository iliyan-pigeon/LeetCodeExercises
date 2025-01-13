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
