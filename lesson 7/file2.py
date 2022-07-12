# Compute the total price of the stock where the total price
# is the sum of the price of an item multiplied by the quantity of this exact item.

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
# Create a function which takes as input two dicts with structure mentioned above
# then computes and returns the total price of stock.
def total_price(s, p):
    sum = 0
    for n in s.keys():
        sum += s[n] * p[n]
    print(sum)
total_price(stock, prices)