# Technical Test for Papernest

Two programs:
- converter: convert a csv file containing location data in lamber93 format to gps data (lat, lon) 
- api: an api to search for available operators at an address.

## Install dependencies
```bash
pip install -r requirements.txt
```

## Usage of converter
```bash
python src/converter/main.py [CSV FILE PATH]
```
ths csv file must have header like:
```csv
Operateur;X;Y;2G;3G;4G
```
Where :
- Operateur: operator code.
- X and Y are lamber93 location
- 2G, 3G, 4G: "1" If these networks are available, "0" if not.

## Run the API
```bash
./script/run_api.sh
```
The API documentation is located at /docs

## Run the tests
```bash
./script/run_tests.sh
```
