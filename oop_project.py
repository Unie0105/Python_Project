from bank_accounts import *

Muge=BankAccount(1000, "Muge")
Eli=BankAccount(2000, "Eli")

Muge.getBalance()
Eli.getBalance()

Muge.deposit(500)

Eli.withdraw(10000)
Eli.withdraw(10)

Eli.transfer(100, Muge)

Stockia=InterestRewardsAcct(1000, "Stockia")

Stockia.getBalance()

Stockia.deposit(100)

Stockia.transfer(100, Eli)

Rino=SavingsAcct(1000, "Rino")

Rino.getBalance()

Rino.deposit(100)

Rino.transfer(100, Muge)




