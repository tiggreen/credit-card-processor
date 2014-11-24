"""
Author: Tigran Hakobyan
Class: ProcessorTest. A test class for the credit card processor. 
"""
import sys
import os.path
import unittest

from creditcard import *
from luhn import *
from processor import *


class ProcessorTest(unittest.TestCase):
	
	def setUp(self):
		# valid credit card
		c1 = CreditCard("Tigran", "379098446439330", 3500, 0)
		# invalid card
		c2 = CreditCard("Jack", "9999888877776666", 1500, None)
		# valid credit card
		c3 = CreditCard("James", "346328571294543", 1500, 0)
		self.cards = [c1, c2, c3]
	
	def test_credit_card_increase(self):
		self.cards[0].increase(1000)
		self.assertEqual(self.cards[0].balance, 1000)
		self.cards[0].increase(2000)
		self.assertEqual(self.cards[0].balance, 3000)
		self.cards[0].increase(1000)
		# exceeds the limit so we ignore the charge.
		self.assertEqual(self.cards[0].balance, 3000)
		# charges against Luhn 10 invalid cards are ignored
		self.cards[1].increase(1000)
		self.assertEqual(self.cards[1].balance, None)
		self.assertEqual(self.cards[2].balance, 0)
	
	def test_credit_card_decrease(self):
		self.cards[2].decrease(1200)
		self.assertEqual(self.cards[2].balance, -1200)
		self.cards[2].decrease(300)
		self.assertEqual(self.cards[2].balance, -1500)
		
	def test_credit_card_is_valid(self):
		self.assertTrue(self.cards[0].is_valid_card())
		self.assertFalse(self.cards[1].is_valid_card())
		self.assertTrue(self.cards[2].is_valid_card())
	
	def test_luhn_10_algorithm(self):
		self.assertFalse(Luhn.validate("9999888877776666"))
		self.assertFalse(Luhn.validate("1234567890123456"))
		self.assertTrue(Luhn.validate("4111111111111111"))
		self.assertTrue(Luhn.validate("4087371973812"))
		self.assertTrue(Luhn.validate("4916900753925"))
		self.assertTrue(Luhn.validate("5578936309030720"))
	
	def test_get_real_value_from_dollar(self):
		self.assertEqual(Processor.get_real_value("$1000"), 1000)
		self.assertEqual(Processor.get_real_value("$0"), 0)
		self.assertEqual(Processor.get_real_value("$20"), 20)


if __name__ == '__main__':
	unittest.main()