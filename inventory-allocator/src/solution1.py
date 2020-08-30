from Warehouse import Warehouse, is_Subset
from typing import List


# simple assumtion, cost is depend on item quantity
def findCheapest_simple(order_origin: dict, supply: List[Warehouse]):
    order = order_origin.copy()  # make a deep copy of original order
    ret = []
    for warehouse in supply:    # iterate through warehouse, checking every single match
        inventory = warehouse.inventory
        warehouse_name = warehouse.name
        if is_Subset(order_origin, inventory):
            return [{warehouse_name: order_origin}]

        warehouse_order = {}
        for k in list(order):   # update inventory of both order_copy and inventory
            if k in inventory:
                if order[k] > inventory[k]:
                    warehouse_order[k] = inventory[k]
                    order[k] = order[k] - inventory[k]
                    del inventory[k]
                elif order[k] < inventory[k]:
                    warehouse_order[k] = order[k]
                    inventory[k] = inventory[k] - order[k]
                    del order[k]
                else:
                    warehouse_order[k] = order[k]
                    del order[k]
                    del inventory[k]
        if len(warehouse_order):    # if there is a much, add that match to final result
            ret.append({warehouse_name: warehouse_order})

    ret.sort(key=lambda x: list(x)[0])  # sort base on warehouse's name
    if order:
        return []
    else:
        return ret
