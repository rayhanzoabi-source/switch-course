accounts = {
    'a': 150,
    'b': 50,
    'c': 50
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
    account = get_account(account_name)
    if account is not None:
        account += amount

transfer("a", "c", 50)
deposit("b", 50)
print(accounts)
# what is the bug?