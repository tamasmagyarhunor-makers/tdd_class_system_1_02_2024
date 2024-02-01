class Person():
    def __init__(self):
        self.backpack = []

    def add_item_to_backpack(self, item):
        if item == "":
            raise Exception("Please provide an item to put in the backpack!")
        self.backpack.append(item)