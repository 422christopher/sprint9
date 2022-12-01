# import pandas as pd

# # We will "instantiate" a DataFrame class into an 'object'
# df = pd.DataFrame({'a':[1,2,3], 'b':[4,5,6]})

# if __name__ == '__main__':
#     # the following are "variables" within a class,
#     # which we call 'attributes'
#     # print(df.shape)
#     # print(df.columns)
#     # print(df.index)
#     # print(df.dtypes)

#     # the functions within a class,
#     # are called "methods"
#     print(df.head())
#     print(df.isnull().sum())
#     print(df.describe())
#     # a method for a "Series" object, aka 'column'
#     # which lives inside of a DataFrame object
#     print(df['a'].value_counts())

# classes always start with 'class'
class Wallet:

    # first thing to run when we make a new class
    # outline the required input from the user here
    # the self is an automatic argument that gets passed in by python
    # once the class is instantiated with a specific name.
    # the init method holds all basic attributes for the class.
    def __init__(self, initial_amount=0):
        # save the user-provided initial_amount as an attribute
        # self refers to whatever object I'm working with.
        # the name.balance command will return the initial ammount value
        self.balance = initial_amount

    # spend_cash method
    def spend_cash(self, amount):
        # you can't spend more than you have
        if self.balance < amount:
            return 'not enough money'
        else:
            self.balance -= amount
            return f'remaining balance: {self.balance}'

    def add_cash(self, amount):
        self.balance += amount
        return f"new balance of: {self.balance}"

    # __repr__ method
    # change show the 'object' looks when it is printed out
    # the presence of the self keyword allows me to access or
    # modify class attribute within this function
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"
    
if __name__ == '__main__':
    wallet1 = Wallet(100)
    print(wallet1.add_cash(60))
    print(wallet1.balance)