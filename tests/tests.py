import unittest
from credit_analyzer import check_credit

class TestCreditAnalyzer(unittest.TestCase):

    def test_poor_credit(self):
        self.assertEqual(check_credit(300), "Poor")
        self.assertEqual(check_credit(579), "Poor")

    def test_fair_credit(self):
        self.assertEqual(check_credit(580), "Fair")
        self.assertEqual(check_credit(669), "Fair")

    def test_good_credit(self):
        self.assertEqual(check_credit(670), "Good")
        self.assertEqual(check_credit(739), "Good")

    def test_very_good_credit(self):
        self.assertEqual(check_credit(740), "Very Good")
        self.assertEqual(check_credit(799), "Very Good")

    def test_excellent_credit(self):
        self.assertEqual(check_credit(800), "Excellent")
        self.assertEqual(check_credit(850), "Excellent")

    def test_invalid_score(self):
        self.assertEqual(check_credit(299), "Invalid score")
        self.assertEqual(check_credit(851), "Invalid score")

if __name__ == "__main__":
    unittest.main()