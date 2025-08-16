class Basic:
    def __init__(self, x = 20, y = 8):
        self.x = x
        self.y = y
    
    def Addition(self):
        return self.x + self.y
    
    def Subtraction(self):
        return self.x - self.y
    
    def Times_table(self):
        for i in range(1, self.y):
            print("%i * %i = %i" % (i, self.y, (i*self.y)))

b = Basic()
b.Addition()
b.Subtraction()
b.Times_table()