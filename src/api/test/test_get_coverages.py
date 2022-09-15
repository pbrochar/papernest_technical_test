import unittest
from api.get_coverages import get_coverage_from_address
from api.address_not_found_error import AddressNotFoundError
from api.network_model import Networks, Coverage
from api.convert_networks_code import convert_network_code_to_name

class TestGetCoverages(unittest.TestCase):
    def setUp(self):
        self.good_address = "14 rue Halle 75014 Paris"
        self.bad_address = "bad_address"
        self.coverages = {
            "SFR": Coverage(g2=False, g3=True, g4=False),
            "Orange": Coverage(g2=True, g3=True, g4=True),
            "Free mobile": Coverage(g2=False, g3=True, g4=True),
            "Bouygues Telecom": Coverage(g2=True, g3=True, g4=True),
        }
        self.good_networks = Networks(available_networks=self.coverages)
        self.test_network_code = "01"
        self.good_network_name = "Orange"
        
    def test_get_coverages_should_raise_address_not_found_error(self):
        self.assertRaises(
            AddressNotFoundError, get_coverage_from_address, self.bad_address
        )

    def test_get_coverages_shloud_return_networks(self):
        networks = get_coverage_from_address(self.good_address)
        self.assertEqual(networks, self.good_networks)

    def test_convert_network_code_should_convert(self):
        network_name = convert_network_code_to_name(self.test_network_code)
        self.assertEqual(network_name, self.good_network_name)