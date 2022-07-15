# Compute the total price
# of the stock where the total price is the sum of the price of an item
# multiplied by the quantity of this exact item.


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
keys = list(stock.keys())
total_price = {
    keys[0]: stock['banana']*prices['banana'],
    keys[1]: stock['apple']*prices['apple'],
    keys[2]: stock['orange']*prices['orange'],
    keys[3]: stock['pear']*prices['pear']
}
print(total_price)
