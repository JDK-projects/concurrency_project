
from test_class import Test
from unittest import TestCase
from mock import Mock

class Test_Test(TestCase):

    def test_result(self):
        test = Test(12,23)
        self.assertEqual(35, test.result())