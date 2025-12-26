
''' 
File Name Generator and Search Utility

This script generates mock file names based on specific naming conventions
(Project, Region, Site, Sources, Date, and Version) and provides a utility 
to filter these names using keywords.
'''

import random

# --- Global Constants (Naming Conventions) ---
PROJECTS = ["STARBURST", "GALAXY"]
REGIONS = ["NAM", "SAM", "EMEA", "APAC"]
SITES = ["siteA", "siteB", "siteC", "siteD"]
SOURCES = ["DEV", "PROD", "BACKUP", "TEST"]
FILE_EXTENSIONS = [".csv", ".json", ".txt",
                   ".xls", ".parquet", ".feather", ".hdf"]
# VERSION  # will be of the type ["v01", "v002", "v003"]
# DATE # will be of the ISO format: YYYYMMDD = 20251225


def generate_filenames_path(no_of_files: int = 10):
    '''
    Generates a list of randomized file names following a standard schema.

    Schema: PROJECT_REGION_SITE_SOURCE_YYYYMMDD_HHMMSS_VERSION.EXTENSION

    Args:
        no_of_files (int): The number of filenames to generate. Defaults to 10.

    Returns:
        list[str]: A list of generated filename strings.
    '''

    files = []
    for _ in range(no_of_files+1):
        filename = (
            f"{random.choice(PROJECTS)}_"
            f"{random.choice(REGIONS)}_"
            f"{random.choice(SITES)}_"
            f"{random.choice(SOURCES)}_"
            f"{random.choice([2025, 2026])}{random.randint(1, 12):02}{random.randint(1, 30):02}_"
            f"{random.randint(0, 23):02}{random.randint(0, 59):02}{random.randint(0, 59):02}_"
            f"V00{random.randint(1, 5)}"
            f"{random.choice(FILE_EXTENSIONS)}"
        )
        files.append(filename)
    return files


def filter_filenames(file_list: list[str], filter_keyword: str):
    """
    Filters and prints filenames containing a specific keyword.

    Args:
        file_list (list[str]): The list of filenames to search through.
        filter_keyword (str): The substring to search for within each filename.
    """
    print(f"\nSearching for files containing: '{filter_keyword}'")

    for fname in file_list:
        if fname.find(filter_keyword) != -1:
            print(fname)


def main():
    """
    Entry point for the script. Handles user input and execution flow.
    """

    # 1. Generate Files
    generated_files = generate_filenames_path(count)
    print("\n--- Generated Files ---")
    print("\n".join(generated_files))

    # 2. Filter Files
    keyword = input(
        "\nEnter keyword to filter by (default 'PROD'): ").strip() or "PROD"
    filter_filenames(generated_files, keyword)


if __name__ == "__main__":
    main()
