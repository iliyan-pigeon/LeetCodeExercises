class MinStack(object):

    def __init__(self):
        self.object = []

    def push(self, val):
        self.object.append(val)

    def pop(self):
        self.object.pop()

    def top(self):
        return self.object[-1]

    def getMin(self):
        return min(self.object)
