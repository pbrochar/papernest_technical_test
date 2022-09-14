import requests
from network_model import Coverage, Networks
import math
import csv
from pathlib import Path
from address_not_found_error import AddressNotFoundError
from convert_networks_code import convert_network_code_to_name

FRANCE_ADDRESSES_API = "https://api-adresse.data.gouv.fr/search/"
DATA_FILE = Path("../../data/transformed_data.csv")

def get_networks_from_coordonates(
    latitude: float,
    longitude: float,
) -> Networks:
    '''
    Search in `DATA_FILE`  and compares the gps location with the searched location.
    If :
    - one of the networks (2g, 3g, 4g) is available,
    - The operator is not yet in the list of found operators
    - The location is close (+- 10km)

    Then we consider that the network is available and it is added to the list
    '''
    coverages = {}
    networks_already_found = []
    with open(DATA_FILE, "r") as data_file:
        coverages_data = csv.reader(data_file, delimiter=";")
        next(coverages_data)
        for row in coverages_data:
            if (
                any([int(row[3]), int(row[4]), int(row[5])])
                and not row[0] in networks_already_found
                and math.isclose(latitude, float(row[1]), abs_tol=0.1)
                and math.isclose(longitude, float(row[2]), abs_tol=0.1)
            ):
                    networks_already_found.append(row[0])
                    coverages[convert_network_code_to_name(row[0])] = Coverage(
                        g2=row[3],
                        g3=row[4],
                        g4=row[5],
                    )
    return Networks(available_networks=coverages)


def get_coverage_from_address(address: str) -> Networks:
    '''
    With an adress, call the France Addresses API
    If an address is found: call `get_networks_from_coordonates` to get coverages of this address.
    Else the json is empty so IndexError is raise and this function raise custom AddressNotFoundError
    '''
    response = requests.get(
        FRANCE_ADDRESSES_API,
        params={
            "q": address,
            "limit": 1,
            "autocomplete": 0,
        },
    )
    response.raise_for_status()
    data = response.json()
    try:
        latitude = data["features"][0]["geometry"]["coordinates"][0]
        longitude = data["features"][0]["geometry"]["coordinates"][1]
    except IndexError:
        raise AddressNotFoundError
    return get_networks_from_coordonates(latitude, longitude)
