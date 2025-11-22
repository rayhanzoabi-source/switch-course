accounts = {
    'a': 120,
    'b': 0,
    'c': 30
}

def get_account(account_name):
    if account_name not in accounts:
        raise KeyError(f"No such account: {account_name}")
    return accounts[account_name]

def transfer(from_acc, to_acc, amount):
    if get_account(from_acc) < amount:
        return
    accounts[from_acc] -= amount
    accounts[to_acc] += amount

def deposit(account_name, amount):
    try:
    account = accounts.get(account_name)
    accounts[accounts] += amount
    

transfer("a", "c", 20)
deposit("b", 150)
transfer("b", "c", 50)

# Let's print the account balances to see the results
for account, balance in accounts.items():
    print(f"Account {account}: ${balance}")