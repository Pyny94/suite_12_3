import unittest
import Test_12_11
import tests_12_2

testST = unittest.TestSuite()

testST.addTest(unittest.TestLoader().loadTestsFromTestCase((Test_12_11.RunnerTest)))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase((tests_12_2.TournamentTest)))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)