import unittest
import spro

class DecoratorTestCase(unittest.TestCase):
    def setUp(self):
        self.chance = 50
        self.value = "Default Value"
    def tearDown(self):
        pass
    def WithChanceTest(self):
        self.assertTrue(some_fn = with_chance()(some_fn))
        self.assertTrue(some_fn =  with_chance()())
if __name__ == '__main__':
    unittest.main()
