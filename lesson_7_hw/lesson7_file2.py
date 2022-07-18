#Input data:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock_prices = dict()
for key in stock:
    stock_prices.update({key: stock[key] * prices[key]})

print(stock_prices)