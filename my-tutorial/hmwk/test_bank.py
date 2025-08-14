import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):
    """Test the Bank Account class"""
    def setUp(self):
        self.b = BankAccount(100)
    def test_deposit(self):
        self.assertEqual(self.b.deposit(50), 50)

    def test_withdraw(self):
        self.assertEqual(self.b.withdraw(30), 70)

    def test_display_balance(self):
        self.assertEqual(self.b.account_balance, 100)

if __name__ == '__main__':
    unittest.main()