class MyQueue(object):

    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()
        else:
            return self.stack_out.pop()
        
    def peek(self):
        """
        :rtype: int
        """
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]
        else:
            return self.stack_out[-1]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.stack_out and not self.stack_in:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
