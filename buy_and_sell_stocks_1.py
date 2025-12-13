prices=[ 6 , 7, 8 ,1 , 3, 6]
max_profit= 0
profit = 0
min_price= float('inf')
for price in prices:
    if price < min_price:
        min_price= profit

    profit = price - min_price

    if profit > max_profit:
        max_profit = profit
print(profit)
