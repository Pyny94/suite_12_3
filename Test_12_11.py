import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        r = Runner("Test walk")
        for i in range(10):
            r.walk()
        self.assertEqual(r.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        r= Runner("Test run")

        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100) \


    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        r1 = Runner("Runner 1")
        rr2 = Runner("Runner 2")
        for i in range(10):
            r1.run()
            rr2.walk()
        self.assertNotEqual(r1.distance, rr2.distance)

if __name__ == '__main__':
    unittest.main()

