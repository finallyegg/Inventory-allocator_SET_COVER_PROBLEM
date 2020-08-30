from itertools import combinations
from Warehouse import Warehouse, is_Subset
from typing import List
from solution1 import findCheapest_simple


# combine a list of warehouse into one single big 'warehouse'
def combineSuppliers(suppliers: List[Warehouse]) -> (dict, int):
    ret = {}
    # and compute their total shipping cost (assume shipping cost is independent on item quantity)
    total_cost = 0
    for supplier in suppliers:
        total_cost += supplier.cost
        for e, v in supplier.inventory.items():
            if e not in ret:
                ret[e] = v
            else:
                ret[e] += v
    return ret, total_cost


def add_cost_index(supply_list: List[Warehouse]) -> None:
    for i in range(len(supply_list)):
        supply_list[i].cost = i+1


def findCheapest_complex(order: dict, supply: List[Warehouse]):
    min_cost = float('inf')
    min_cost_list = []
    add_cost_index(supply)
    for i in range(1, len(supply)+1):
        # use python build in function to compute every combination from 1 to n of the supplier warehouse
        for combined in list(combinations(supply, i)):
            single_combined, cost = combineSuppliers(combined)
            if is_Subset(order, single_combined) and cost < min_cost:
                min_cost = cost
                min_cost_list = combined
    return findCheapest_simple(order, min_cost_list)
