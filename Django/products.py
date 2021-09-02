from functools import reduce
products=[
    {"p_name":"complan","mrp":200,"avl_qty":50},
    {"p_name":"horliks","mrp":250,"avl_qty":10},
    {"p_name":"bournvita","mrp":220,"avl_qty":0},
    {"p_name":"nutri","mrp":200,"avl_qty":100},
    {"p_name":"mylo","mrp":100,"avl_qty":0}
]
# print all product names in the shop
product_name=list(map(lambda item:item["p_name"],products))
print(product_name)

# print all products aailable in the shop
aval_product=list(filter(lambda item:item["avl_qty"]>0,products))
print(aval_product)

# print out of stock product
out_stock=list(filter(lambda item:item["avl_qty"]==0,products))
print(out_stock)

# print costly products
prices=list(map(lambda item:item["mrp"],products))
print(max(prices))
cost_price=reduce(lambda price1,price2:price1 if price1>price2 else price2,prices)
print(cost_price)