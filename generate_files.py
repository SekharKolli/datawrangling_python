
''' 
File Name Generator and Search Utility

This script generates mock file names based on specific naming conventions
(Project, Region, Site, Sources, Date, and Version) and provides a utility 
to filter these names using keywords.
'''

import random
import re

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
    for _ in range(no_of_files):
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


def filter_filenames_method01(file_list: list[str], filter_keyword: str):
    """
    Identifies files using basic string membership testing via the find() method.

    This is a procedural approach that iterates through the list and uses the 
    low-level string method to check for substring existence.

    Args:
        file_list (list[str]): A list of generated filename strings.
        filter_keyword (str): The specific substring to locate.
    """
    # -----Method 01-----: Using string method find() to identify substring
    print("\n-----Method 01-----: Using string method find() to identify substring")
    print(
        f"Searching {len(file_list)} file(s) containing: '{filter_keyword}'")

    for fname in file_list:
        if fname.find(filter_keyword) != -1:
            print(f"{fname.replace(filter_keyword, "📍"+filter_keyword+"📍")}")


def filter_filenames_method02(file_list: list[str], filter_keyword: str):
    """
    Filters files using list comprehension and highlights matches in the output.

    This method demonstrates 'Pythonic' filtering using a list comprehension 
    and the 'in' operator for better readability and performance. It 
    visually highlights the match by wrapping the keyword in brackets.

    Args:
        file_list (list[str]): A list of generated filename strings.
        filter_keyword (str): The specific substring to locate and highlight.
    """
    # -----Method 02-----: Using list comprehension and in to filter
    print("\n-----Method 02-----: Using list comprehension and in to filter")
    print(
        f"Searching {len(file_list)} file(s) containing: '{filter_keyword}'")
    matches = [fname for fname in file_list if filter_keyword in fname]

    if matches:
        for match in matches:
            print(f"{match.replace(filter_keyword, "📍"+filter_keyword+"📍")}")
        print(f"{len(matches)} file(s) found matching that keyword.")
    else:
        print(" No files found matching that keyword.")


def filter_filenames_method03(file_list: list[str], filter_keyword: str):
    """
    Filters files using functional programming and regular expressions.

    Utilizes the filter() function with a lambda expression and the re.search() 
    engine. This approach is highly scalable for complex pattern matching 
    beyond simple substrings.

    Args:
        file_list (list[str]): A list of generated filename strings.
        filter_keyword (str): A string or regex pattern to match against filenames.
    """
    # -----Method 03-----: Using lambda, filter(), regex filter
    print("\n-----Method 03-----: Using lambda, filter(), regex filter")
    print(
        f"Searching {len(file_list)} file(s) containing: '{filter_keyword}'")

    matches = list(filter(lambda fname: re.search(
        filter_keyword, fname), file_list))

    if matches:
        for match in matches:
            print(f"{match.replace(filter_keyword, "📍"+filter_keyword+"📍")}")
        print(f"{len(matches)} file(s) found matching that keyword.")
    else:
        print(" No files found matching that keyword.")


def main():
    """
    Entry point for the script. Handles user input and execution flow.
    """

    # 1. Generate Files
    count = int(input("Enter number of files to generate (default 10): ") or 10)
    generated_files = generate_filenames_path(count)
    print("\n--- Generated Files ---")
    print("\n".join(generated_files))

    # 2. Filter Files
    keyword = input(
        "\nEnter keyword to filter by (default 'PROD'): ").strip() or "PROD"

    filter_filenames_method01(generated_files, keyword)
    filter_filenames_method02(generated_files, keyword)
    filter_filenames_method03(generated_files, keyword)


if __name__ == "__main__":
    main()
