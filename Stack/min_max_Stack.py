class MinStack:
    def __init__(self, ):
        self.stack = [] #main stack
        self.min_stack = [] #min stack
        self.max_stack = [] # max stack

    def push(self,data):
        self.stack.append(data)
        if self.min_stack:
            self.min_stack.append(min(data,self.min_stack[-1]))
        else:
            self.min_stack.append(data)
        if self.max_stack:
            self.max_stack.append(max(data,self.max_stack[-1]))
        else:
            self.max_stack.append(data)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
            self.max_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def getmin(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1

    def getMax(self):
        if self.max_stack:
            return self.max_stack[-1]
        else:
            return -1

stack = MinStack()
stack.push(1)
stack.push(5)
stack.push(50)
stack.push(0)
print(stack.getmin())
print(stack.getMax())