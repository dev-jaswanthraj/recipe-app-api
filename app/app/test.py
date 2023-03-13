""" 
Same Tests.
"""

from django.test import SimpleTestCase
from app import calc

class CalcTest(SimpleTestCase):
    """Test the calc module."""

    def test_add_number(self):
        """Test adding number together."""

        res = calc.add(5, 9)

        self.assertEqual(res, 14)

    def test_substract_number(self):
        """Test substracting numbers."""

        res = calc.substract(20, 7)

        self.assertEqual(res, 13)