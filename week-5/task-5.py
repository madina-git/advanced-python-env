class BankAccount:
    def __init__(self, owner, balance=0):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit must be positive!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Cannot withdraw this amount!")

    def get_balance(self):
        return self.__balance


# --- Пример работы ---
account = BankAccount("Alice", 1000)

account.deposit(1000)
account.withdraw(200)
account.withdraw(50)  # Нельзя
print(account.get_balance())  # Выведет 1300
