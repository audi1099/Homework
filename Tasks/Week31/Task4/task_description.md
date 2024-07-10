# Описание задачи

## Задача

Создать класс "Bank" для управления банковским счетом. Реализовать методы для открытия/закрытия счета, пополнения/снятия средств и проверки баланса.

### Класс `Bank`

```python
class Bank:
    def __init__(self):
        self.balance = 0
        self.open = False

    def open_account(self):
        if not self.open:
            self.open = True
            print("Счет открыт.")
        else:
            print("Счет уже открыт.")

    def close_account(self):
        if self.open:
            self.balance = 0
            self.open = False
            print("Счет закрыт.")
        else:
            print("Счет уже закрыт.")

    def deposit(self, amount):
        if self.open:
            if amount > 0:
                self.balance += amount
                print(f"Пополнение на сумму {amount} прошло успешно.")
            else:
                print("Неверная сумма для пополнения.")
        else:
            print("Нельзя пополнить закрытый счет.")

    def withdraw(self, amount):
        if self.open:
            if 0 < amount <= self.balance:
                self.balance -= amount
                print(f"Снятие на сумму {amount} прошло успешно.")
            else:
                print("Недостаточно средств на счете или неверная сумма для снятия.")
        else:
            print("Нельзя снять деньги с закрытого счета.")
