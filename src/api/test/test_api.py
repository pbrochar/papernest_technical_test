import unittest
from fastapi.testclient import TestClient
from api.main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)
        self.good_address = "14 rue Halle 75014 Paris"
        self.api_good_response = {
            "available_networks":
                {
                    "SFR": {"2G":False,"3G":True,"4G": False},
                    "Orange":{"2G":True,"3G":True,"4G":True},
                    "Free mobile":{"2G":False,"3G":True,"4G":True},
                    "Bouygues Telecom":{"2G":True,"3G":True,"4G":True}
			}
        }
        self.bad_address = "bad_address"
    
    def test_api_should_return_good_response(self):
        response = self.client.get("/", params={
			"q": self.good_address
		})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), self.api_good_response)
    
    def test_api_should_return_http_error_404(self):
        response = self.client.get("/", params={
			"q": self.bad_address
		})
        self.assertEqual(response.status_code, 404)