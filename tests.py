import unittest
import windowsCost

class WinTest(unittest.TestCase):
    def testCalc1(self):
        result = windowsCost.GetWindowCost("2", "1", 1.3, 1.5, 0.5)
        self.assertEqual(result, 9620)

    def testCalc2(self):
        result = windowsCost.GetWindowCost("2", "2", 1.3, 1.5, 0.5)
        self.assertEqual(result, 10149)

    def testCalc3(self):
        result = windowsCost.GetWindowCost("3", "1", 1.8, 1.5, 0.5)
        self.assertEqual(result, 15012)

    def testCalc4(self):
        result = windowsCost.GetWindowCost("3", "2", 1.8, 1.5, 0.5)
        self.assertEqual(result, 15542)

    def testCalc5(self):
        with self.assertRaises(AssertionError):
          windowsCost.GetWindowCost("10", "2", 1.8, 1.5, 0.5)

    def testCalc6(self):
        with self.assertRaises(AssertionError):
          windowsCost.GetWindowCost("3", "10", 1.8, 1.5, 0.5)
        
if __name__ == '__main__':
    unittest.main()
