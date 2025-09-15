class A:
    def __init__(self,id,name,salary):
        self.id = id
        self.name=name
        self.salary=salary

    def first(self):
        print(self.id)
        print(self.name)
        print(self.salary)

    def second(self):
        print(self.id)
        print(self.name)
        print(self.salary)

obj = A(1,"ashutosh",20000)
obj.first()
obj = A(2,"vaibhav",50000)
obj.second()

