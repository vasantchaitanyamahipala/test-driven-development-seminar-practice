import unittest
def add(a,b):
    return a+b

class testfunction(unittest.TestCase):
    def testpostive(self):
         self.assertEqual(add(1, 2), 3)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()



