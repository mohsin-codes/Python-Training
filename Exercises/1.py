good_credit = False
price = 1000000
down_payment = 0
if good_credit:
    down_payment = price * (10 / 100)
else:
    down_payment = price * (20 / 100)

print("The down payment is : ", down_payment)