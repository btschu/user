class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

brandon_schumacher = User("Brandon Schumacher", "brandon@gmail.com")
fred_smith = User("Fred Smith", "fred@gmail.com")
jill_doe = User("Jill Doe", "jill@gmail.com")

brandon_schumacher.make_deposit(1000)
brandon_schumacher.make_deposit(500)
brandon_schumacher.make_deposit(700)
brandon_schumacher.make_withdrawal(500)
brandon_schumacher.display_user_balance()

fred_smith.make_deposit(500)
fred_smith.make_deposit(800)
fred_smith.make_withdrawal(300)
fred_smith.make_withdrawal(200)
fred_smith.display_user_balance()

jill_doe.make_deposit(2500)
jill_doe.make_withdrawal(500)
jill_doe.make_withdrawal(200)
jill_doe.make_withdrawal(400)
jill_doe.display_user_balance()

brandon_schumacher.transfer_money(jill_doe, 100)
brandon_schumacher.display_user_balance()
jill_doe.display_user_balance()


#! Instructor's solution
# class User:

#     def __init__(self, name):
#         self.name = name
#         self.amount = 0

#     def make_deposit(self, amount):
#         self.amount += amount

#     def make_withdrawl(self,amount):
#         self.amount -= amount

#     def display_user_balance(self):
#         print(f"User: {self.name}, Balance: {self.amount}")

#     def transfer_money(self,amount,user):
#         self.amount -= amount
#         user.amount += amount
#         self.display_user_balance()
#         user.display_user_balance()


# adrien = User("Adrien")
# nibbles = User("Mr. Nibbles")
# benny_bob = User("Benny Bob")

# adrien.make_deposit(100)
# adrien.make_deposit(200)
# adrien.make_deposit(50)
# adrien.make_withdrawl(45)
# adrien.display_user_balance()

# nibbles.make_deposit(1000)
# nibbles.make_deposit(1000)
# nibbles.make_withdrawl(500)
# nibbles.make_withdrawl(300)
# nibbles.display_user_balance()

# benny_bob.make_deposit(1500)
# benny_bob.make_withdrawl(1000)
# benny_bob.make_withdrawl(5000)
# benny_bob.make_withdrawl(3000)
# benny_bob.display_user_balance()


# nibbles.transfer_money(400, adrien)