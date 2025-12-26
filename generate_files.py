
''' This python file creates and generates the names of the files. '''

import random

# File Naming Conventions
PROJECT = ["STARBURST", "GALAXY"]
REGIONS = ["NAM", "SAM", "EMEA", "APAC"]
SITE = ["siteA", "siteB", "siteC", "siteD"]
CONTENT = ["DEV", "PROD", "BACKUP", "TEST"]
FILE_EXTENSION = [".csv", ".json", ".txt",
                  ".xls", ".parquet", ".feather", ".hdf"]
# VERSION  # will be of the type ["v01", "v002", "v003"]
# DATE # will be of the ISO format: YYYYMMDD = 20251225


def generate_filenames_path(no_of_files: int = 10):
    '''Generates a set of filesnames (default :10) as a list'''
    files = []
    for _ in range(no_of_files+1):
        filename = (
            f"{random.choice(PROJECT)}_"
            f"{random.choice(REGIONS)}_"
            f"{random.choice(SITE)}_"
            f"{random.choice(CONTENT)}_"
            f"{random.choice([2025, 2026])}{random.randint(1, 12):02}{random.randint(1, 30):02}_"
            f"{random.randint(0, 24):02}{random.randint(0, 60):02}{random.randint(0, 60):02}_"
            f"V00{random.randint(1, 5)}"
            f"{random.choice(FILE_EXTENSION)}"
        )
        files.append(filename)
    return files


def filter_filesnames(file_list: list[str], filter_keyword: str):
    '''
    filters the files based on the keyword

    :param file_list: Description
    :param filter_keyword: Description
    '''
    print(f"List of files with the keyword {filter_keyword=}")
    for fname in file_list:
        if fname.find(filter_keyword) != -1:
            print(fname)


def main():
    '''   Function to run the example and ask for use inputs    '''

    files_to_generate = int(input(
        "How many files Names would you like to generate :")) or 10

    file_list = generate_filenames_path(files_to_generate)
    print(str(file_list).replace(",", "\n"))

    filter_keyword = input(
        "List the keyword that you would like to find :") or "PROD"
    filter_filesnames(file_list, filter_keyword)


if __name__ == "__main__":
    main()
