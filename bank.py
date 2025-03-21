from exceptions import AccountNotFoundError, AccountExist
from account import BankAccount
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

    def transfer(self, from_acc: str, to_acc: str, amount: float) -> None:

        try:
            if from_acc in self.accounts and to_acc in self.accounts:
                logger.info(f'Переведено {amount} руб. со счета № {from_acc} на счет № {to_acc}.')
            else:
                raise AccountNotFoundError
        except AccountNotFoundError:
            if from_acc not in self.accounts and to_acc not in self.accounts:
                logger.error(f'Данные счета {from_acc}, {to_acc} не существуют!')
            elif from_acc not in self.accounts:
                logger.error(f'Счет № {from_acc} не существует!')
            else:
                logger.error(f'Счет № {to_acc} не существует!')

#ff = Bank()
#dd = BankAccount('cчёт № SFD-001', 1000)
#dd1 = BankAccount('cчёт № SFD-003', 1000)
#ff.add_account(dd)
#ff.add_account(dd1)
#ff.accounts_all()
#ff.transfer('cчёт № SFD-003', 'cчёт № SFD-002', 500)






