import unittest
import main
from io import StringIO

input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

class Tests(unittest.TestCase):

    def test_extract_seeds(self):

        expected_seeds=[79, 14, 55, 13]
        seeds = main.extract_seeds(input)
        self.assertEqual(seeds, expected_seeds)

    def test_extract_seeds_single_line(self):

        expected_seeds=[79, 14, 55, 13]
        seeds = main.extract_seeds("seeds: 79 14 55 13")
        self.assertEqual(seeds, expected_seeds)

    def test_is_new_category_category(self):

        string = "seed-to-soil map:"
        result = main.is_new_category(string)
        self.assertEqual(result, True)

    def test_is_new_category_numbers(self):

        string = "50 98 2"
        result = main.is_new_category(string)
        self.assertEqual(result, False)

    def test_parse_one_category(self):

        soil_category = [[50, 98, 2], [52, 50, 48]]
        fertilizer_category = [[0, 15, 37], [37, 52, 2], [39, 0, 15]]
        water_category = [[49, 53, 8], [0, 11, 42], [42, 0, 7], [57, 7, 4]]
        light_category = [[88, 18, 7], [18, 25, 70]]
        temperature_category = [[45, 77, 23], [81, 45, 19], [68, 64, 13]]
        humidity_category = [[0, 69, 1], [1, 0, 69]]
        location_category = [[60, 56, 37], [56, 93, 4]]

        stream = StringIO(input)

        result_one = main.parse_one_category(stream)
        self.assertEqual(result_one, soil_category)

        result_two = main.parse_one_category(stream)
        self.assertEqual(result_two, fertilizer_category)

        result_three = main.parse_one_category(stream)
        self.assertEqual(result_three, water_category)

        result_four = main.parse_one_category(stream)
        self.assertEqual(result_four, light_category)

        result_five = main.parse_one_category(stream)
        self.assertEqual(result_five, temperature_category)

        result_six = main.parse_one_category(stream)
        self.assertEqual(result_six, humidity_category)

        result_seven = main.parse_one_category(stream)
        self.assertEqual(result_seven, location_category)

        result_eight = main.parse_one_category(stream)
        self.assertEqual(result_eight, [])

    def test_part_one(self):

        stream = StringIO(input)

        result = main.part_one(stream)

        self.assertEqual(result, 35)

    def test_pairing(self):

        string = "2880930400 17599561 549922357 200746426 1378552684 43534336 155057073 56546377 824205101 378503603 1678376802 130912435 2685513694 137778160 2492361384 188575752 3139914842 1092214826 2989476473 58874625"

        expected_result = [(2880930400, 17599561), (549922357, 200746426), (1378552684, 43534336), (155057073, 56546377), (824205101, 378503603), (1678376802, 130912435), (2685513694, 137778160), (2492361384, 188575752), (3139914842, 1092214826), (2989476473, 58874625)]

        values = list(map(int, string.split()))

        result = list(zip(values[::2], values[1::2]))

        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
