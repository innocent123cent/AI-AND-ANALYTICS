supermarket = {"milk": {"quantity":20,"price": 1.19},
"bisuits": {"quantity":32,"price": 1.45},
"butter": {"quantity":20,"price": 2.29},
"cheese": {"quantity":15,"price": 1.90},
"bread": {"quantity":15,"price": 2.59},
"cookies": {"quantity":20,"price": 4.49},
"yorghurt": {"quantity":18,"price": 3.65},
"apples": {"quantity":30,"price": 3.35},
"oranges": {"quantity":40,"price": 0.99},
"bananas": {"quantity":23,"price": 1.29},
}
total_cost=0
for k,v in supermarket.items():
    total_cost +=v["quantity"]*v["price"]
    print("Tatal cost",total_cost)

