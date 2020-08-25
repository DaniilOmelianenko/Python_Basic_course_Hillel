from dataclasses import dataclass


@dataclass
class Value:
    amount: float
    currency: str


class ATM:
    bank_name = 'Mono'

    def __init__(self, amount):
        self.initial_amount = self._validate_amount(amount)
        self.max_limit = 10000
        self.currency = 'UAH'
        self.curr_map = {'UAH': 1.0, 'USD': 27.8, 'EUR': 32.2}

    def _validate_amount(self, amout):
        if amout < 0:
            raise ValueError
        return amout

    def add_money(self, value, cur='UAH'):
        if cur in {'USD', 'EUR', 'UAH'}:
            value = float(value * (self.curr_map[cur]))
        else:
            return ValueError
        self.initial_amount += value
        return self.initial_amount

    def withdraw(self, amount, cur='UAH'):
        if self.initial_amount < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError('More than I can get')
        if cur in {'USD', 'EUR', 'UAH'}:
            amount = float(amount * (self.curr_map[cur]))
        else:
            raise ValueError('Wrong Currency')
        self.initial_amount -= amount
        return self.initial_amount
