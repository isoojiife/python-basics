#Grocery Billing Queue
total = 0
customer = 1

while customer <= 2:
    print("Customer", customer)

    item = 1
    customer_total = 0

    while item <= 3:
        price = int(input("Enter the price: £"))
        customer_total = customer_total + price
        item = item + 1

    print("Customer total: £", customer_total)

    total = total + customer_total
    customer = customer + 1

print("All customers total: £", total)