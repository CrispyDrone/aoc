import unittest
import main

input = [
        [([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]),   8],
        [([13, 32, 20, 16, 61], [61, 30, 68, 82, 17, 32, 24, 19]), 2],
        [([1, 21, 53, 59, 44],  [69, 82, 63, 72, 16, 21, 14, 1]),  2],
        [([41, 92, 73, 84, 69], [59, 84, 76, 51, 58, 5, 54, 83]),  1],
        [([87, 83, 26, 28, 32], [88, 30, 70, 12, 93, 22, 82, 36]), 0],
        [([31, 18, 13, 56, 72], [74, 77, 10, 23, 35, 67, 36, 11]), 0],
]

class Tests(unittest.TestCase):

    def test_reads_all_numbers(self):
        input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"

        result = main.extract_numbers(input)

        self.assertEqual(result[0], [41, 48, 83, 86, 17])
        self.assertEqual(result[1], [83, 86, 6, 31, 17, 9, 48, 53])

    def test_calculate_points(self):

        for numbers, expected_result in input:
            with self.subTest({ "numbers": numbers, "expected result": expected_result}):

                result = main.calculate_points(numbers)

                self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
