class Category:
    name = ''
    ledger = []

    def __init__(self, category_name):
        self.name = category_name
        self.ledger = []

    def __str__(self):
        output = ''
        output += self.name.center(30, '*') + '\n'
        
        for i in self.ledger:
            output += i['description'].ljust(23)[:23]
            s = format(i['amount'], '.2f')
            output += f'{s}'.rjust(7)
            output += '\n'
        
        balance = format(self.get_balance(), '.2f')
        output += f'Total: {balance}'
        return output

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount):
            return False

        amount = amount * -1
        self.ledger.append({'amount': amount, 'description': description})
        return True
    
    def get_balance(self):
        balance = 0
        for i in self.ledger:
            balance += i['amount']
        return balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def check_funds(self, amount):
        balance = 0
        for i in self.ledger:
            balance += i['amount']

        if balance < amount:
            return False
        else:
            return True

def create_spend_chart(categories):
    lines = []
    percentages = []
    spent = []

    for i in categories:
        for j in i.ledger:
            if j['amount'] > 0:
                deposit = j['amount']
        spent.append(deposit - i.get_balance())

    spent_total = sum(spent)
    for i in spent:
        percentages.append(int(i / spent_total * 10))

    lines.append('Percentage spent by category')
    for i in range(11):
        s = format((100 - (10 * i)), '>3') + '| '
        for j in percentages:
            if (10 - i) <= j:
                s += 'o  '
            else:
                s += '   '
        lines.append(s)
    width = 4 + (3 * (len(categories) - 1))
    lines.append(('-' * width).rjust(14))

    max_length = 0
    for i in categories:
        max_length = max(max_length, len(i.name))
    for i in range(max_length):
        s = '     '
        for j in range(len(categories)):
            if len(categories[j].name) > i:
                s += categories[j].name[i] + '  '
            else:
                s += '   '
        lines.append(s)

    output = ''
    for i in lines:
        output += i + '\n'
    output = output.rstrip('\n')
    return output