"""
Author: Tigran Hakobyan
Class: CreditCard. Represents a credit card object.
"""

class CreditCard:
	
	def __init__(self, name, number, limit, balance):
		self.name = name
		self.number = number
		self.limit = limit
		self.balance = balance
		
	"""
	Increase the balance of the card by the given amount.
	"""
	def increase(self, amount):
		# Charges against Luhn 10 invalid cards are ignored.
		if self.is_valid_card():
			if amount + self.balance <= self.limit:
				self.balance += amount
	
	"""
	Decrease the balance of the card by the given amount.
	"""
	def decrease(self, amount):
		if self.is_valid_card():
			self.balance -= amount
	
	"""
	Check if the credit card is valid. Credit card
	is invalid if its balance is None.
	"""
	def is_valid_card(self):
		return self.balance is not None
