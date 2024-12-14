#!/usr/bin/env python

# command line example $python3 pre_process_Q2_updated.py "14100328.csv" > "extract_Q2.csv"

'''
pre_process_Q2_updated.py
Author(s): Hamza Irshad (1261380)
Earlier contributors(s): Daman Kumar (1306900), Jacob Good (1300566), Ryan Sass-Gregoire(1230473), Hamza Irshad (1261380)

Project: Milestone 3 Pre Process Updated
Date of Last Update: Mar 18, 2024.

Functional Summary:
    This script filters a CSV file for job vacancies specifying non-university certificates
    or diplomas as the required education level and outputs relevant information for further analysis,
    replacing missing or empty values with 0. Now including job vacancy characteristics in the output.

Commandline Parameters: 1
    argv[0] = this python program   
    argv[1] = name of the input file containing the data

References:
    Data files from https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032805
'''

import sys
import csv


def main(argv):
    if len(argv) != 2:
        print("Usage: pre_process_Q2.py <input_file.csv>")
        sys.exit(1)

    input_file = argv[1]

    try:
        # Open the file for reading
        file_data = open(input_file, encoding='utf-8-sig')
        reader = csv.reader(file_data)

        headers = next(reader)
        # Adding Job vacancy characteristics to the updated headers
        updated_headers = ['REF_DATE', 'GEO', 'National Occupational Classification',
                           'Job vacancy characteristics', 'Statistics', 'VALUE']
        print(','.join(updated_headers))

        for row in reader:
            if "Non-university certificate or diploma" in row[4]:
                # Check for empty or ".." value and replace with 0
                value_index = headers.index('VALUE')
                if row[value_index] == '' or row[value_index] == '..':
                    row[value_index] = '0'

                # Extracting only the relevant columns for the output
                updated_row = []
                for col in updated_headers:
                    updated_row.append(row[headers.index(col)])

                processed_row = []
                for cell in updated_row:
                    # Handling cells with commas
                    if ',' in cell:
                        processed_row.append(f'"{cell}"')
                    else:
                        processed_row.append(cell)
                print(','.join(processed_row))

        # Close the file after processing
        file_data.close()

    except IOError as err:
        print(f"Error opening file '{input_file}': {err}", file=sys.stderr)
        sys.exit(1)

main(sys.argv)
