'''
The below code simulates a real banking system with options to open a new bank savings account or do operations with an existing bank account.
'''

import random #Random library for generating random 5 digit account number
import time

# class Banking():
# 	def __init__(self):
# 		accounts = {}

global accounts
accounts = {}

class NewAccount():

	def addAccount(self, username, initialDeposit):
		self.username = username
		self.initialDeposit = initialDeposit
		self.accountno = random.choice([x for x in range(10000,99999) if x not in list(accounts.keys())])
		accounts[self.accountno] = {'AccountName':self.username, 'AmountAvailable':self.initialDeposit}
		print("A new account has been created with the Account Number {} under the Account Name {}".format(self.accountno, self.username))
		
class ExistingAccount(NewAccount):
	def __init__(self,username, accountno):
		super().__init__()
		self.username = username
		self.accountno = accountno

	def checkAccount(self):
		if self.accountno in list(accounts.keys()):
			if accounts[self.accountno]['AccountName'] == self.username:
				return True
			else:
				print('The Account Name and Account Number combination does not match. Please check!')
				return False
		else:
			print("The Account Number you provided does not match our records. Please try again!")
			return False
			
	def DisplayDetails(self):
		print("The details for the Account Number {} are given below: \n".format(self.accountno))
		print("Account Name: ", self.username, '\n')
		print("Available Amount: ", accounts[self.accountno]['AmountAvailable'], '\n')

	def Withdraw(self, wamt):
		if wamt < accounts[self.accountno]['AmountAvailable']:
			accounts[self.accountno]['AmountAvailable'] = accounts[self.accountno]['AmountAvailable'] - wamt
			print('An amount of {} has been withdrawn from the account number {}. The current amount in the account is {}'.format(wamt, self.accountno,accounts[self.accountno]['AmountAvailable'] ))
		else:
			print("You do not have sufficient funds to withdraw the requested amount")

	def Deposit(self, damt):
		accounts[self.accountno]['AmountAvailable'] = accounts[self.accountno]['AmountAvailable'] + damt
		print('An amount of {} has been deposited to the account number {}. The current amount in the account is {}'.format(damt, self.accountno, accounts[self.accountno]['AmountAvailable']))

#HCI starts
print()
print("Welcome to the HIPSTER BANK!",'\n')
time.sleep(2)

while True:
	print()
	print("Please enter 1 to create a new Savings Account or enter 2 to access an existing Savings Account or enter 3 to quit")
	while True:
		try:
			useroption = int(input())
			break
		except:
			print("Please enter a valid input")
	if useroption == 1:
		print("Please enter your Name")
		accountName = input()
		print("Please enter the amount of initial deposit you\'d like to make towards your account")
		while True:
			try:
				initdeposit = int(input())
				break
			except:
				print("Please enter a valid amount")

		newacc = NewAccount()
		newacc.addAccount(accountName, initdeposit)

	elif useroption == 2:
		print("Please enter the name of the account you want to access")
		AccountName = input()
		print("Please enter the number of the account you want to access")
		while True:
			try:
				accountNumber = int(input())
				break
			except:
				print("The account number should be a 5-digit number")

		exisacc = ExistingAccount(AccountName,accountNumber)
		if exisacc.checkAccount():
			print()
			print("The account has been verified",'\n')
		else:
			continue

		print("""Please tell us what would you like to do with the account?\n1. Press 1 to withdraw\n2. Press 2 to deposit\n3. Press 3 to display the available balance\n4. Press 4 to quit""")
		userchoice = int(input())
		if userchoice == 1:
			print("Please enter the amount you\'d like to withdraw from the account")
			wamt = int(input())
			exisacc.Withdraw(wamt)
		elif userchoice == 2:
			print("Please enter the amount you\'d like to deposit into the account")
			damt = int(input())
			exisacc.Deposit(damt)
		elif userchoice == 3:
			exisacc.DisplayDetails()
		elif userchoice == 4:
			quit()
	elif useroption == 3:
		quit()
	else:
		print("Please enter a valid input")
		








