# Exercise 2: Variables
# https://gitlab.labranet.jamk.fi/ttc2030/basics-of-programming/-/blob/master/exercises/exercise02.md

"""
2.3.
[x] Declare a variable which is used to store bank account balance in euro (start balance of 2000 €). 
[x] Print current balance into the console. 
[x] Ask from user how many euro will be added to the balance. 
[x] Then ask how many cents are added to the balance. 
[x] Print the balance after user requested changes are made.
"""

bank_balance_eur = 2000

print('Bank account balance: {} €'.format(bank_balance_eur))

add_euro = int(input('How many euro will be added to the balance? '))
add_cent = int(input('How many cents will be added to the balance? '))

bank_balance_eur += add_euro
bank_balance_eur += add_cent / 100

print('Bank account balance: {} €'.format(bank_balance_eur))

print()