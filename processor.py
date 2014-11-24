"""
Author: Tigran Hakobyan
Class: Processor. Represents the credit card processor run by the user. 
"""
import fileinput, sys

from creditcard import *
from luhn import *


class Processor:
	
	"""
	Every Processor object has a dictionary (hashtable) of (name, card) tuples.
	Name uniquely identifies the credit card account in the dictionary.
	"""
	all_cards = dict()
	
	"""
	Print the last summary of the processor.
	"""
	def print_summary(self):
		# Sorting the all_cards by name of the card.
		for el in sorted(Processor.all_cards):
			name = Processor.all_cards[el].name
			if Processor.all_cards[el].balance is not None:
				balance = "$" + str(Processor.all_cards[el].balance)
			else:
				balance = "error"
			print(name + ": " + balance)
	
	"""
	Create a new credit card for a given name, card number, and limit.
	"""
	def add(self, name, number, limit):
		balance = 0
		# if card number is not valid then balance = None
		if not self.is_valid_card(number):
			balance = None
		card = CreditCard(name, number, limit, balance)
		# Add the current credit card object into the hashtable.
		Processor.all_cards[name] = card
		
	"""
	Implement the charge command. Increase the balance of the card.
	"""
	def charge(self, name, amount):
		# what id card is not present. 
		# Check if card exist in the hashtable.
		if name in Processor.all_cards:
			card = Processor.all_cards[name]
			card.increase(amount)
	
	"""
	Implement the credit command. Decrease the balance of the card.
	"""
	def credit(self, name, amount):
		if name in Processor.all_cards:
			card = Processor.all_cards[name]
			card.decrease(amount)
	
	"""
	Check if the given credit number is valid using
	Luhn's algorithm.
	"""
	def is_valid_card(self, number):
		# Primary validation check of the number. 
		if len(number) > 19:
			return False
		else:
			return Luhn.validate(number)
			
	"""
	E.g. take $1000 and return 1000.
	"""
	@classmethod
	def get_real_value(cls, amount):
		if amount is None:
			return None
		return int(amount[1:])
	
	"""
	Take a file or stdin and simulate the credit card processor.
	"""
	def process(self, user_input):
		for line in user_input:
			try:
				line_array = line.strip().split()
				# if line is not empty
				if line_array:
					command = line_array[0]
					if command == "Summary":
						return
					name = line_array[1]
					if command == "Add":
						number = line_array[2]
						limit = line_array[3]
						p.add(name, number, Processor.get_real_value(limit))
					elif command == "Charge":
						amount = line_array[2]
						p.charge(name, Processor.get_real_value(amount))
					elif command == "Credit":
						amount = line_array[2]
						p.credit(name, Processor.get_real_value(amount))
					else:
						pass
			except IndexError:
				print("Something went wrong while processing your input.")
		
if __name__ == '__main__':
	p = Processor()
	if len(sys.argv) < 2:
		p.process(sys.stdin)
	else:
		filename = sys.argv[1]
		try:
			p.process(open(filename))
		except IOError:
			print("Can't open the file.")
	
	# Printing the summary of the processor.	
	p.print_summary()
			
	
	