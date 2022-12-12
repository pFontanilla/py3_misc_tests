class item1(object):

    def __init__(self):
        self.x = 2

class itemEater(object):

    def eat(self):
        self.item1.x = 5

    def __init__(self, item1):
        self.item1 = item1


a = item1()
b = itemEater(a)

print(a.x)
print(b.item1.x)
b.eat()
print("Ate")
print(a.x)
print(b.item1.x)