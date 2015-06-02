Author: Tigran Hakobyan


----------------------------

#### Usage

To run the program with a file run:
`python processor.py <filename>`

To run the program with stdin run:
`python processor.py`
While you're in stdin mode in order to see the final summary and exit 
the program type "Summary" and hit enter.


To run all unit tests run:
`python -m unittest -v`


#### Design decisions
The program consists of 4 different classes and one of them is the Test class to test the mothods that I think is worth testing. I have a CreditCard object which has an account name, number, balance and limit instance variables. Luhn class has only one static method called validate which uses Luhn 10's algorithm to check if the given credit number is valid or not. Please note, that even if credit card number is invalid we still create an object but with a balance=None. The Processor class is the class that has main() in it and has to be run by user. I used Python's built-in unittest module to implement my test class. 



#### Future work
  * We can't have two credit card account with the same name 
  * We don't have a type for a credit card (VISA, MASTERCARD, etc), or close an account.
