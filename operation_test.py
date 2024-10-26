import unittest
import operation


class TestOperation(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)

    def test_add(self):
        self.assertEqual(operation.Operation().add(10, 5), 15)
        self.assertEqual(operation.Operation().add(2, 3), 5)
        self.assertEqual(operation.Operation().add(0, 0), 0)


if __name__ == "__main__":
    unittest.main()
