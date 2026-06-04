"""
Вариант 5. Блок 1.
Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки.
Добавьте методы для вычисления процентных начислений и снятия денег.
"""

class Bank:

    def set_data(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * (self.interest_rate / 100)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount
        return 0


account = Bank()
account.set_data(150000, 8.5)

print(account.balance)
print(account.interest_rate)

interest = account.calculate_interest()
print(interest)

taken = account.withdraw(50000)
print(taken)
print(account.balance)

failed_take = account.withdraw(200000)
print(failed_take)
