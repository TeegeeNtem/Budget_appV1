class Budget:

    def __init__ (self,category,amount,balance=0):
        self.category=category
        self.amount=amount
        self.balance=balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print('Added {} to the balance' .format(deposit_amount)) 

    def withdrawal(self, withdrawal_amount):
        if(self.balance >= withdrawal_amount):
            self.balance -= withdrawal_amount
            print('transaction approved')    
        else:
            print('insufficient funds')

    def transfer(self,amount,category):
        self.balance -= amount
        category.balance += amount
        return f'Transferred {self.amount} from {self.category} \nYour current balance: {category.balance}'

    def get_balance(self):
        print(self.balance)       

    def __str__(self):
        return f'category: {self.category} \nBalance: {self.balance}' 
 
### creating instances ###

food = Budget('food',500)
clothing = Budget('clothing',300)
entertainment = Budget('entertainment',200)

#print(budget_1.__dict__)
#print(budget_2.__dict__)
#print(budget_3.__dict__)

#print(food.deposit(1000))
#print(food)
#print(food.withdrawal(1000))
#print(food)
#print(food.withdrawal(100)ls
#print(food.get_balance())

#print(clothing.deposit(700))
#print(clothing)
#print(clothing.withdrawal(1000))
#print(clothing)
#print(clothing.withdrawal(100))
#print(clothing.get_balance())

#print(entertainment.deposit(700))
#print(entertainment)
#print(entertainment.withdrawal(1000))
#print(entertainment)
#print(entertainment.withdrawal(100)
#print(entertainment.get_balance())
#print(entertainment.transfer(500, food))

print(food.transfer(500, clothing))
print(entertainment.transfer(200, clothing))
print(clothing)
