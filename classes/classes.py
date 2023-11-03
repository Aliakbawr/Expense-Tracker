class Group:
    def __init__(self, name):
        self.name = name
        self.transactions = []
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def edit_name(self, name):
        self.name = name


class Person:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def total_expenses(self):
        return sum(expense.amount for expense in self.expenses)


class Expense:
    def __init__(self, description, amount, participants):
        self.description = description
        self.amount = amount
        self.participants = participants

    def individual_share(self):
        return self.amount / len(self.participants)


person1 = Person("Alice")
person2 = Person("Bob")
person3 = Person('Reza')
amount_spent = 90
expense1 = Expense("Dinner", 100, [person1, person2])
expense2 = Expense("Lunch", amount_spent, [person1, person2, person3])
#
# person1.add_expense(expense1)
# person2.add_expense(expense2)
person1.add_expense(expense2)
# person3.add_expense(expense2)

# Calculate total expenses for each person
print(f"{person1.name}'s total expenses: {person1.total_expenses()}")
print(f"{person2.name}'s total expenses: {person2.total_expenses()}")
print(f"{person3.name}'s total expenses: {person3.total_expenses()}")

# Calculate individual share for each expense
print(f"{expense1.description} individual share: {expense1.individual_share()}")
print(f"{expense2.description} individual share: {expense2.individual_share()}")
