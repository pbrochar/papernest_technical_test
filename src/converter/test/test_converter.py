import unittest

import pytest
from converter.main import lamber93_to_gps, get_number_of_lines, convert_data
from pathlib import Path
import filecmp
import os
import pytest

TEST_DATA_CONVERTED_PATH = Path('./src/converter/test/test_data/test_short_transformed_data.csv')
TEST_DATA_LAMBER93_PATH = Path('./src/converter/test/test_data/test_short_lamber93_data.csv')
OUTPUT_FILE = Path('./src/converter/test/test_data/test_short_for_compare.csv')

class TestConverter(unittest.TestCase):
    
    def setUp(self):
        self.lamber93_x = 102980
        self.lamber93_y = 6847973
        self.gps_lon = -5.08885611530134
        self.gps_lat = 48.4565745588299
        self.test_file_number_of_lines = 9
    
    @pytest.mark.filterwarnings('ignore')
    def test_lamber93_convert_should_be_exact(self):
        lon, lat = lamber93_to_gps(self.lamber93_x, self.lamber93_y)
        self.assertEqual(lon, self.gps_lon)
        self.assertEqual(lat, self.gps_lat)
    
    def test_get_number_line_should_return_good_response(self):
        lines = get_number_of_lines(TEST_DATA_CONVERTED_PATH)
        self.assertEqual(lines, self.test_file_number_of_lines)
    
    @pytest.mark.filterwarnings('ignore')
    def test_convert_file_should_convert_file(self):
        convert_data(TEST_DATA_LAMBER93_PATH, OUTPUT_FILE)
        self.assertTrue(filecmp.cmp(TEST_DATA_CONVERTED_PATH, OUTPUT_FILE))
        os.remove(OUTPUT_FILE)