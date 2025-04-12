import account
from exceptions import AccountNotFoundError, AccountExist
from account import BankAccount, SavingsAccount
from loguru import logger


class Bank:
    def __init__(self):
        self.accounts = {}


    def add_account(self, account: BankAccount) -> None:
        try:

            if account._account_number not in self.accounts:
              self.accounts[account._account_number] = account._balance
              logger.info(f'Добавлен новый счет № {account._account_number}: {account._balance} руб.')
            else:
              raise AccountExist
        except AccountExist:
            logger.error(f'Счет {account._account_number} уже существует!')

    def accounts_all(self):
        logger.info(self.accounts)
        return self.accounts

    def transfer(self, from_acc: BankAccount, to_acc: BankAccount, amount: float) -> None:

        try:
            #баланс заложен в self.accounts
            if from_acc._account_number in self.accounts and to_acc._account_number in self.accounts:
                logger.info(f'Перевод {amount} руб. со счета № {from_acc._account_number} на счет № {to_acc._account_number}.')

                if from_acc._balance > amount:
                    from_acc.withdraw(amount)
                    to_acc.deposit(amount)
                    self.accounts[from_acc._account_number] = from_acc._balance
                    self.accounts[to_acc._account_number] = to_acc._balance
                else:
                    from_acc.withdraw(amount)

            else:
                raise AccountNotFoundError
        except AccountNotFoundError:
            if from_acc._account_number not in self.accounts and to_acc._account_number not in self.accounts:
                logger.error(f'Данные счета {from_acc._account_number}, {to_acc._account_number} не существуют!')
            elif from_acc._account_number not in self.accounts:
                logger.error(f'Счет № {from_acc._account_number} не существует!')
            else:
                logger.error(f'Счет № {to_acc._account_number} не существует!')


#
# ff = Bank()
# dd = BankAccount('SFD-001', 1500)
# dd1 = SavingsAccount('SFD-003', 1000)
# ff.add_account(dd)
# ff.add_account(dd1)
# ff.accounts_all()
# ff.transfer(from_acc=dd, to_acc=dd1, amount=200)
# dd.get_balance()
# dd1.get_balance()
# ff.accounts_all()







