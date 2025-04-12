from loguru import logger
import matplotlib.pyplot as plt
from exceptions import InsufficientFundsError, LimitBalance
from pprint import pprint


class BankAccount:
    def __init__(self, account_number: str, balance: float)-> None:
        #номер счета
        self._account_number = account_number
        #текущий баланс
        self._balance = balance
        #список истории транзакций
        self._transaction_history = {}
        self.lis = []
        self.operation = []
        self.number = 0

    #пополнение счета
    def deposit(self, amount: float) -> None:

        self._balance += amount
        self.number += 1
        self.operation.append(self.number)
        self.add_transaction(f'{self.number} | Счёт № {self._account_number} | пополнение: {amount} | Баланс')


    #списание со счета
    def withdraw(self, amount: float) -> None:
        try:
            if amount < self._balance:
                self._balance -= amount
                self.number += 1
                self.operation.append(self.number)
                self.add_transaction(f'{self.number} | Счёт № {self._account_number} | снятие: {amount} | Баланс')
            else:
                raise InsufficientFundsError
        except InsufficientFundsError:
            logger.error(f'Недостаточно средств на балансе счета № {self._account_number}. Пополните баланс для снятия.')



    def add_transaction(self, operation: str) -> None:
        self._transaction_history[operation] = self._balance


    def get_transaction_history(self) -> dict[str]:

        logger.info(self._transaction_history)
        return self._transaction_history
        # for k in self._transaction_history.items():
        #     logger.info(list(k))
        #pprint(self._transaction_history)


    def get_balance(self) -> float:
        logger.info(f'Баланс счета № {self._account_number}: {self._balance} руб.')
        return self._balance


    def __str__(self) -> str:
        logger.info(f'Текущий баланс по счету № {self._account_number}: {self._balance} руб.')
        return (f'Текущий баланс по счету № {self._account_number}: {self._balance} руб.')


    def visualize_balance(self) -> None:
        y = list(self._transaction_history.values()) #ось y
        x = self.operation
        plt.figure(figsize=(6, 5))
        # строим график
        plt.plot(x, y)
        plt.xlabel('Ось х')  # Подпись для оси х
        plt.ylabel('Ось y')  # Подпись для оси y
        bbox_properties = dict(
            boxstyle="Round, pad=0.1",
            ec="SandyBrown",
            fc="w",
            ls="-",
            lw=1
        )
        plt.title('Динамика баланса', fontsize=13, bbox=bbox_properties,
                  color='rebeccapurple', fontstyle="italic", fontweight="bold")
        plt.plot(x, y, color='mediumpurple', marker='o', ms=7, mec='mediumblue')
        # сетка
        plt.grid()
        plt.xlabel('Номер операции')
        plt.ylabel('Баланс, руб.')
        plt.show()



class SavingsAccount(BankAccount):

    def withdraw(self, amount: float) -> None:
        try:
            if amount <= self._balance*0.9:
                self._balance -= amount
                self.number += 1
                self.operation.append(self.number)
                self.add_transaction(f'{self.number} | Счёт № {self._account_number} | снятие: {amount} | Баланс')
            else:
                raise LimitBalance
        except LimitBalance:
            logger.error(f'Сумма {amount} руб. превышает лимит ({round(self._balance*0.9)} руб.) снятия от баланса.')



#
# dd = BankAccount("SA-101", 1000)

# dd.get_balance()
# dd.deposit(100)
# dd.withdraw(50)
# dd.deposit(70)
# dd.withdraw(13)
# dd.get_transaction_history()
# # dd.visualize_balance()

