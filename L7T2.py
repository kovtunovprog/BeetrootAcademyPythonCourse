stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    "dragonfruit": 10  # added manually
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

total_price = {}
stock_price = 0

# In case there's no price on item in stock, use if
for k, v in stock.items():
    if k not in prices:
        print(f'NOTICE! {k} has no price in the pricelist!')
        continue
    total_price.update({k: v * prices[k]})
    stock_price += stock[k] * prices[k]

print(f'Value of each item is: {total_price}')
print(f'Value of stock is: {stock_price}')
