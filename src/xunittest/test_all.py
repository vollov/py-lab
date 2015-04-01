import unittest
from test_a import TestA
from test_b import TestB
from testcase.test_c import TestC

def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestA))
    test_suite.addTest(unittest.makeSuite(TestB))
    test_suite.addTest(unittest.makeSuite(TestC))
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())