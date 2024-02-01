class Person():
    def __init__(self):
        self.backpack = []

    def add_item_to_backpack(self, item):
        if item == "":
            raise Exception("Please provide an item to put in the backpack!")
        self.backpack.append(item)

person = Person()
person.add_item_to_backpack("coke")
person.add_item_to_backpack("watch")
person.add_item_to_backpack("book")

print(person.backpack)