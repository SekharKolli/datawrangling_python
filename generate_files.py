
''' This python file creates and generates the names of the files. '''

import random

# File Naming Conventions
REGIONS = ["NAM", "SAM", "EMEA", "APAC"]
SITE = ["siteA", "siteB", "siteC", "siteD"]
CONTENT = ["RawData", "PROD", "BACKUP", "UAT"]
FILE_EXTENSION = [".csv", ".json", ".txt",
                  ".xls", ".parquet", ".feather", ".hdf"]
# VERSION  # will be of the type ["v01", "v002", "v003"]
# DATE # will be of the ISO format: YYYYMMDD = 20251225


def generate_filenames_path(no_of_files: int = 10):
    '''Generates a set of filesnames (default :10) as a list'''
    files = []
    for _ in range(no_of_files+1):
        filename = (
            f"{random.choice(REGIONS)}_"
            f"{random.choice(SITE)}_"
            f"{random.choice(CONTENT)}_"
            f"{random.choice([2025, 2026])}{random.randint(1, 12)}{random.randint(1, 30)}_"
            f"V00{random.randint(1, 5)}"
            f"{random.choice(FILE_EXTENSION)}"
        )
        files.append(filename)
    return files


file_list = generate_filenames_path()

print(file_list)
