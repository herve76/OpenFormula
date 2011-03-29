import unittest

from stats import MAX, MIN, AVERAGE, SUMPRODUCT


class TestOpenFormulaFunctions(unittest.TestCase):

#Statistics functions
    def test_max(self):
        self.assertEqual(MAX("A1:B2"), "MAX([.A1:.B2])")
	self.assertEqual(MAX("A1:B2","C3:D4"),"MAX([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, MAX, 2)

    def test_min(self):
        self.assertEqual(MIN("A1:B2"), "MIN([.A1:.B2])")
	self.assertEqual(MIN("A1:B2","C3:D4"),"MIN([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, MIN, 2)

    def test_average(self):
	self.assertEqual(AVERAGE("A1:B2"),"AVERAGE([.A1:.B2])")
	self.assertEqual(AVERAGE("A1:B2","C3:D4"), 
                                             "AVERAGE([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, AVERAGE, 2)

    def test_sumproduct(self):
	self.assertEqual(SUMPRODUCT("A1:B2"),"SUMPRODUCT([.A1:.B2])")
	self.assertEqual(SUMPRODUCT("A1:B2","C3:D4"),
                                          "SUMPRODUCT([.A1:.B2] ; [.C3:.D4])")
        self.assertRaises(TypeError, SUMPRODUCT, 2)

if __name__ == '__main__':
    unittest.main()


                          


                          
