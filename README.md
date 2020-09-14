# Inventory allocator

###### By: Zeping He

&NewLine;

##### Due to the vague definition of the cost function, Cost can either be the fixed shipping cost from each location (that is, shipping cost is independent on item quantity), or the cost is based on item quantity (shipping cost from a warehouse depends on the item quantities).

&NewLine;
&NewLine;

##### Thus, I proposed two methods for this question

- Method One: Assume shipping cost is independent, assign index of warehouse array as cost value. Then try to minimize the output cost. (Typical set cover problem, which is **NP-hard**)
- Method Two: Assume shipping cost is dependent on item quantity, always select warehouse with less shipping cost unless there exists a warehouse can cover all item in an order

&NewLine;

---

## Method One `findCheapest_Complex` (Set Cover Problem)

- Use index+1 as a cost value for WareHouse
  -- ex: given Warehouse Array:`[{ name: owd, inventory: { apple: 5 } }, { name: dm, inventory: { apple: 5 }}] `
  -- Then: `cost[owd] = 1, cost[dm] = 2`
- Compute all possible combinations (using Python build function `itertools.combination` to create combination list) and then find the min cost.

Algorithm:

- Assign cost index for each Warehouse
- Compute all possible Warehouse combinations
- Find a specific combination that cover all items in order and achieve minimum cost
- Pass combination list to `findCheapest_Simple` get final result

&NewLine;

## Method Two: `findCheapest_Simple` (Simple One)

###### This is a much simple one :

&NewLine;

Algorithm:

- Iterate entire warehouse list to see if there is a single warehouse can cover full list of order
  -- if yes, return that warehouse
- iterate warehouse list and select every single item that have a match in order

&NewLine;

## Difference of two method in practice:

#### Test Cases:

- ##### order: `= {"apple": 10, "banana": 10}`
- ##### warehouses `= [w1:{'apple': 1, 'banana': 2}, w2:{'apple': 5, 'banana': 6}, w3:{'apple': 5, 'banana': 6}]`

&NewLine;

##### Result for Method 1 (Set Cover):

###### ` [{'w2': {'apple': 5, 'banana': 6}}, {'w3': {'apple': 5, 'banana': 4}}]`

##### Reason: ** Assume cost is \***independent**\* on item quantity ** cost for w1: 1, cost for w2: 2, cost for w3: 3, select w2 and w3 will achieve minium cost of 5

&NewLine;

##### Result for Method 2 (Simple):

###### ` [{'a': {'apple': 1, 'banana': 2}}, {'b': {'apple': 5, 'banana': 6}}, {'c': {'apple': 4, 'banana': 2}}]`

##### Reason: ** Assume cost is \***dependent**\* on item quantity **, as long as there is no such warehouse can cover all order, we select warehouse if there is a match

&NewLine;

---

### Run test

\*require python3

You can view and modifiy test case in `test.py`

```sh
$ cd ./src
$ python3 test.py
```

&NewLine;

---

### Input, Output and `Warehouse` Class

| input        | Where               | type                                                                               |
| ------------ | ------------------- | ---------------------------------------------------------------------------------- |
| Warehouse    | src/Warehouse.py    | a python class contains **name** :`str`, **inventory** :`dict`, and **cost**:`int` |
| order_origin | findCheapest_simple | a python `dict`                                                                    |
| supply       | findCheapest_simple | list of `Warehouse` objects                                                        |
| suppliers    | combineSuppliers    | list of `Warehouse` objects                                                        |
