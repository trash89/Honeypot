from brownie import accounts, Attack, Bank, HoneyPot, Logger


def main():
    print("Deploying Honetpot...")
    hp = HoneyPot.deploy({"from": accounts[0]})
    print(f"Honeypot deployed at {hp}")

    print("Deploying Bank with the address of Honeypot...")
    b = Bank.deploy(hp.address, {"from": accounts[0]})
    print(f"Bank deployed at {b}")

    print("Depositing 1 ether into Bank...")
    tx = b.deposit({"from": accounts[0], "value": "1 ether"})
    tx.wait(1)
    print(f"Deposited, Bank.balance()= {b.balance()}")

    print("Depoying Attack with the address of Bank...")
    a = Attack.deploy(b.address, {"from": accounts[1]})
    print(f"Attack deployed at {a}")

    print("Calling Attack.attack() with 1 ether...")
    tx = a.attack({"from": accounts[1], "value": "1 ether"})
    tx.wait(1)
