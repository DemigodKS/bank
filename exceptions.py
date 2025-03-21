import logging


logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s", encoding='UTF-8')

class AccountNotFoundError(Exception):
    pass

class InsufficientFundsError(Exception):

    pass

class LimitBalance(Exception):
    pass

class AccountExist(Exception):
    pass
