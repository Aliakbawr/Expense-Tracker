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


class Member:
    def __init__(self, name):
        self.name = name
        self.expenses = []
        self.groups = []
        self.members = []

    def add_group(self, group):
        self.groups.append(group)

    def add_members(self, member):
        self.members.append(member)

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

    def __str__(self):
        return f'''
        Description: {self.description}
        Amount: {self.amount}
        Participants: {self.participants}'''


def add_group_panel(member):
    group_name = input('Enter groups name:')
    group = Group(group_name)
    member.add_group(group)
    print(f'Group ({group_name}) added successfully')


def add_member_panel(group):
    member_name = input('Type members name:')
    member = Member(member_name)
    group.add_member(member)
    print(f'Member ({member_name}) added to ({group}) successfully')


def add_expense_panel(group):
    expense_name = input('Enter expenses name:')

    i = 1
    print('Select the spender:')
    for member in group:
        print(f'{i}- {member.name}')
        i += 1
    choice = int(input())
    spender: Member = group[(choice - 1)]

    expense_amount = int(input('Enter expenses amount:'))

    expense_participants = []
    print('Choose participants:')
    n = 1
    for member in group:
        print(f'{n}- {member.name}')
        n += 1
        choice = int(input('1)add\t2)next\t3)skip'))
        match choice:
            case 1:
                expense_participants.append(member)
            case 2:
                continue
            case 3:
                break

    expense = Expense(expense_name, expense_amount, expense_participants)
    spender.add_expense(expense)

    print('Expense information:\n' + expense.__str__())


person1 = Member("Alice")
person2 = Member("Bob")
person3 = Member('Reza')
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
