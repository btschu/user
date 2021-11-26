class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(self.name, self.account_balance)

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

user_one = User("Brandon Schumacher", "brandon@gmail.com")
user_two = User("Fred Smith", "fred@gmail.com")
user_three = User("Jill Doe", "jill@gmail.com")

user_one.make_deposit(1000)
user_one.make_deposit(500)
user_one.make_deposit(700)
user_one.make_withdrawal(500)
user_one.display_user_balance()

user_two.make_deposit(500)
user_two.make_deposit(800)
user_two.make_withdrawal(300)
user_two.make_withdrawal(200)
user_two.display_user_balance()

user_three.make_deposit(2500)
user_three.make_withdrawal(500)
user_three.make_withdrawal(200)
user_three.make_withdrawal(400)
user_three.display_user_balance()

user_one.transfer_money(user_three, 100)
user_one.display_user_balance()
user_three.display_user_balance()

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