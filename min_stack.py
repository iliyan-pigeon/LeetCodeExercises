# Solution 1
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


# Solution 2
class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            if top == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None
