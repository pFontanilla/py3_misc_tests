class Item(object):

    def __init__(self, name):
        self.name = name

    def call(self):
        print self.name

item1 = Item(1)
item2 = Item(2)

item2.name = item1.name

item2.name = item2.name + 5

item2.call()
item1.call()