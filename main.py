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
bill3 = BankAccount('SAP-101', 1000)
#создаем счета
bank.add_account(bill1)
bank.add_account(bill2)
bank.add_account(bill3)
#переводим деньги
bank.transfer('SAP-101', 'SSP-120', 250)
#простой счет
bill1.withdraw(2000)
#сберегательный счет
bill2.withdraw(490)
#счета, которого нет
bank.transfer('SAP-101', 'SSP-122', 100)
bank.transfer('SAP-199', 'SSP-122', 100)
bank.transfer('SAP-199', 'SSP-120', 100)
#баланс
bill1.get_balance()
bill2.get_balance()
#визуализация
bill2.deposit(100)
bill2.withdraw(50)
bill2.deposit(70)
bill2.withdraw(13)
bill2.get_transaction_history()
bill2.visualize_balance()




