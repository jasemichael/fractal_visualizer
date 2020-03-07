import unittest

from Testing import TestMandelbrot, TestJulia

suite = unittest.TestSuite()

tests = (TestMandelbrot.TestMandelbrot, TestJulia.TestJulia)
for test in tests:
    suite.addTest(unittest.makeSuite(test))

runner = unittest.TextTestRunner(verbosity=2)
print(runner.run(suite))
