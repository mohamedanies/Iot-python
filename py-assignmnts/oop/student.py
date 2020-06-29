class student:
    def __init__(self, name):
        self.name = name
        self.marks = []
        print('welcome {} to our school'.format(name))
    
    
    def add_marks(self, *mark):
        for i in mark:
            self.marks.append(i)
        
    def avg(self):
        return sum(self.marks)/len(self.marks)
        
std1 = student('mohamed')
print(std1.marks)
std1.add_marks(40,50,60)
print(std1.marks)
print(std1.avg())
