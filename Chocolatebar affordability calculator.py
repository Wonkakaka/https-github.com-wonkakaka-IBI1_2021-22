def f(money, price):
# Create a new function on money and prices.
    X = money//price
# X is the number of the chocolate bar.
    Y = money%price
# Y is the change
    return[X,Y]
# For example:
money = 66
price = 8
print("The number of the chocolate bar and the change are", f(money, price))
#print: The number of the chocolate bar and the change are [8, 2]