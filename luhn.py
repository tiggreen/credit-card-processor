"""
Author: Tigran Hakobyan
Class: Luhn. Represents Luhn class. 
"""
class Luhn:
	
	"""
	Take a credit card number and return true if 
	it's a valid credit card number. Uses Luhn 10's algorithm.  
	"""
	@classmethod
	def validate(cls,number):
		sm = 0
		num_digits = len(number)
		oddeven = num_digits & 1
		for count in range(0, num_digits):
			digit = int(number[count])
			if not ((count & 1) ^ oddeven):
				digit = digit * 2
			if digit > 9:
				digit = digit - 9
				
			sm = sm + digit
		return ((sm % 10) == 0)
		