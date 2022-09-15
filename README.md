#Technical test for Papernest

Two programs:
- converter: converted a csv file containing location data in lamber93 format to gps data (lat, lon) 
- api: an api to search for available operators at an address.

## Install dependencies
```bash
pip install -r requirements.txt
```

## Usage of converter
```bash
python src/converter/main.py [CSV FILE PATH]
```

## Run the API
```bash
./script/run_api.sh
```

## Run the tests
```bash
./script/run_tests.sh
```
