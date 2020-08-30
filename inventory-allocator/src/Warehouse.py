class Warehouse:
    def __init__(self, name: str, inventory: dict = None, cost=0):
        self.name = name
        self.inventory = inventory
        self.cost = cost

    def __str__(self):
        return self.name + ":" + str(self.inventory)

    def __repr__(self):
        return self.name + ":" + str(self.inventory)


def is_Subset(a: dict, b: dict):      # return True if a is a subset of b
    if not len(a) or not len(b):
        return False
    for k, v in a.items():
        if k not in b or b[k] < v:
            return False
    return True
