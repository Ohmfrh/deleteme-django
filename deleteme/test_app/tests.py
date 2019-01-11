import unittest


class Test1(unittest.TestCase):

    def test_pass(self):
        self.assertEqual(0, 0)

    # def test_fail(self):
    #     self.fail('FORCE FAIL')
