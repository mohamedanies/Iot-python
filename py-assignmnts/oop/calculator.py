class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        return self.a + self.b
    def mul(self):
        return self.a * self.b

x = calculator(1,2)
print(x.add())
print(x.mul())