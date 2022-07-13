stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
    "lemon": 15,
    "cherry": 6,
    "tomato": 1,
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
    "tomato": 0,
}
total_price = 0  # count of price
total_products = []  # name of products
for key in stock:
    # total_price += stock[key]*prices[key]
    price_of_product = stock.get(key, 0)*prices.get(key, 0)  # price one type of product
    total_price += price_of_product
    if price_of_product != 0:
        total_products.append(key)
print('Your total price :', total_price, '₴')
print('You get :', total_products)

