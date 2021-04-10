class Budget:

    def __init__(self, name):
        self.name = name
        self.totalBal = 0

    def balance(self):
        return f'{self.name} curent balance is: {self.totalBal}'

    def deposit(self, amountDeposited):
        self.totalBal += amountDeposited
        return f'You deposited {amountDeposited} into {self.name} and current balance is {self.totalBal}'

    def withdrawal(self, amountWithdrawn):
        if amountWithdrawn > self.totalBal:
            return 'Insufficient fund'
        else:
            self.totalBal -= amountWithdrawn
            return f'You withdrew #{amountWithdrawn} and total balance left for {self.name} budget is: {self.totalBal}'

    def transfer(self, amountTransfer, categoryTransferTo):
        if amountTransfer <= self.totalBal:
            self.totalBal -= amountTransfer
            categoryTransferTo.totalBal += amountTransfer
            return f'#{amountTransfer} transfered to {categoryTransferTo.name} category'
        else:
            return 'Insufficient fund'


food = Budget('food')
entertainment = Budget('entertainment')
cloth = Budget('cloth')

# To deposit into a category
food.deposit(3000)
entertainment.deposit(2000)
cloth.deposit(1500)

# To transfer to a other categories
print(food.transfer(500, cloth))
print(food.transfer(1000, entertainment))

# To withdrawal from a category
print(entertainment.withdrawal(100))
print(food.withdrawal(100))
print(cloth.withdrawal(100))

# To print balance
print(food.balance())
print(cloth.balance())
print(entertainment.balance())
