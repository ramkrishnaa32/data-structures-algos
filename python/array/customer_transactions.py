"""
Programming/Algorithm Question (30 - 35 minutes):

You are acting as a bank.  You are given a list of customers' transactions.
The transactions can be either a deposit (positive value) or a withdrawal(negative value).
The initial balance in the bank is 0.
The bank can choose any customer to start serving from the list.
Once a customer is picked, the bank will continue serving the next customer in the list until the bank's balance becomes zero or negative.
At that point, the bank will close.
Your task is to determine the maximum number of customers that can be served by the bank.

For example, given the customer_transactions = [-1, 2, 4, -3, 5, -10, 3, 10, 1],
you need to find the maximum number of customers that can be served by the bank.

The answer in this case is 4 i.e. [ 2, 4, -3, 5]
"""

transctions = [-1, 2, 4, -3, 5, -10, 3, 10, 1]

lenght = len(transctions)
max_customer = 0
arr = []

for i in range(lenght):
    balance = 0
    count = 0
    curr_arr = []
    for j in range(i, lenght):
        balance += transctions[j]
        if balance < 0:
            break
        count += 1
        curr_arr.append(transctions[j])

    print(f"sub-array: {curr_arr}")

    if count > max_customer:
        max_customer = count
        arr = curr_arr.copy()

    print(f"max_customer: {max_customer}, arr: {arr}")

print(max_customer, arr)