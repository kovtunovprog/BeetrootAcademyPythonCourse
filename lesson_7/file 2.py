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

total_price_of_the_stock = 0

for product in stock:
    total_price_of_the_stock += (
            stock[product] * prices[product]
    )

print(total_price_of_the_stock)
