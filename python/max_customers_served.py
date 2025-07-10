"""
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

def max_customers_served(transactions):
    max_count = 0
    best_subarray = []
    n = len(transactions)

    for i in range(n):
        balance = 0
        count = 0
        current_subarray = []
        for j in range(i, n):
            balance += transactions[j]
            if balance < 0:
                break
            current_subarray.append(transactions[j])
            count += 1

        if count > max_count:
            max_count = count
            best_subarray = current_subarray.copy()

    return max_count, best_subarray

transactions = [-1, 2, 4, -3, 5, -10, 3, 10, 1]
max_count, subarray = max_customers_served(transactions)
print("Max customers served:", max_count)
print("Transaction subarray:", subarray)