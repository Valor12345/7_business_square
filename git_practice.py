class A:
    def __init__(self,id,name,salary):
        self.id = id
        self.name=name
        self.salary=salary

    def first(self):
        print(self.id)
        print(self.name)
        print(self.salary)



obj = A(1,"tanmay",20000)
obj.first()
