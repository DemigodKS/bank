from loguru import logger
from bank import Bank
from account import BankAccount, SavingsAccount

logger.add('banking.log', level='INFO',format="{level} - {message}")

with open('banking.log', 'w'):
    pass
#создаем счета

bank = Bank()

bill1 = BankAccount('SAP-101', 1000)
bill2 = SavingsAccount('SSP-120', 500)
#bill3 = BankAccount('SAP-101', 1000)
#создаем счета
bank.add_account(bill1)
bank.add_account(bill2)
#bank.add_account(bill3)
#переводим деньги
bank.transfer(from_acc=bill1, to_acc=bill2, amount=250)
# bill1.get_balance()
# bill2.get_balance()
#простой счет
bill1.deposit(2000)
bill1.withdraw(350)
# #сберегательный счет
bill2.withdraw(490)
bill2.deposit(55)
bank.transfer(from_acc=bill2, to_acc=bill1, amount=330)
# #баланс
bill1.get_balance()
bill2.get_balance()
#
bill2.get_transaction_history()
#bill1.visualize_balance()




