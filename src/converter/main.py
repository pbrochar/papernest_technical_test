import pyproj
import csv
from pathlib import Path
import warnings
import sys
from tqdm import tqdm

warnings.filterwarnings("ignore")

HEADER = ["Operateur", "X", "Y", "2G", "3G", "4G"]
CONVERTED_FILE_NAME = Path("transformed_data.csv")


def lamber93_to_gps(x, y):
    lambert = pyproj.Proj(
        "+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs"
    )
    wgs84 = pyproj.Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
    long, lat = pyproj.transform(lambert, wgs84, x, y)
    return long, lat


def get_number_of_lines(file: Path) -> int:
    '''
    Calculates the number of lines in the source file.
    '''
    with open(file, "r") as file:
        data = csv.reader(file, delimiter=";")
        next(data)
        lines = len(list(data))
    return lines


def convert_data(src_file: Path, dest_file: Path) -> None:
    '''
    This Function is used to:

    - Create a new csv file
    - Convert the data of the base csv file
    - Write to the new file
    
    tqdm is the library used for the progress bar.
    '''
    lines = get_number_of_lines(src_file)
    with open(dest_file, "w") as new_data_file:
        writer = csv.writer(new_data_file, delimiter=";")
        writer.writerow(HEADER)
        with open(src_file, "r") as data_file:
            data = csv.reader(data_file, delimiter=";")
            next(data)
            for row in tqdm(data, total=lines):
                try:
                    long, lat = lamber93_to_gps(row[1], row[2])
                except:
                    continue
                writer.writerow([row[0], long, lat, row[3], row[4], row[5]])


if __name__ == "__main__":
    '''
    Simple CLI to convert data in a Lambert93 csv file to gps data.
    The Header of the source file is :

    "Operator", "X", "Y", "2G", "3G", "4G"
    where X and Y are location data in lambert93 format
    
    Source file must be a .csv file.
    The CLI does not check if the file conforms to the expectations
    '''
    if len(sys.argv) != 2:
        print("Need one argument: csv file path", file=sys.stderr)
        sys.exit(1)
    if Path(sys.argv[1]).exists() and Path(sys.argv[1]).suffix == ".csv":
        convert_data(Path(sys.argv[1]), CONVERTED_FILE_NAME)
    else:
        print("Invalid file", file=sys.stderr)
        sys.exit(1)
