class Item(object):

    def __init__(self, name):
        self.name = name

    def call(self):
        print self.name

class ItemFake(object):

    def __init__(self, name, real):
        self.name = name
        self.call = lambda: real.call()

class utils(object):

    @classmethod
    def incr(cls, item):
        item.name = item.name + 1


list = []

item1 = Item(1)
item2 = Item(2)

list.append(item1)
list.append(item2)

for item in list:
    print(item.name)

print("Modify")
utils.incr(item1)
utils.incr(item2)

for item in list:
    print(item.name)

print("Overwrite Item")

list[1] = Item(77)

item3 = item1

del item1
del item3

for item in list:
    print(item.name)

print("Add item 33")

list.append(Item(33))

# function = lambda: list[2].call()

list[2].call()

print("Replace Item33 in list, keep reference to function from Item 33")

list[2] = ItemFake(44, list[2])

list[2].call() # If '33' is printed, then reference to Item33 still exists

del item2
print("Finished")


