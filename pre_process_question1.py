#!/usr/bin/env python

#command line example $python3 pre_process_question1.py "14100328.csv" > "pre_process_question1.csv"
'''
pre_process_quesiton1.py
  Author(s): Daman Kumar (1306900)
  Earlier contributors(s): Jacob Good (1300566)

  Project: Milestone II Pre Process Data For Quesiton 1
  Date of Last Update: Mar 12, 2024.

  Functional Summary
      pre_process_quesiton1.py takes in a CSV (comma separated version) file. Then filters the data of occupational classification of 
      “Software engineers and designers [2173]”, that further refer to “Avg hourly wage".

      There are expected to be these fields:
        • REF_DATE reference date
        • GEO (Dimension ID 1) geographical region
        • DGUID geographical region ID code
        • National Occupational Classification (Dimension ID 2) one of 692 cate-
            gories as listed in the meta-data file
        • Job vacancy characteristics (Dimension ID 3) e.g. “Full-time”, “Part-time”
        • Statistics (Dimension ID 4) “Job vacancies”, “Proportion of job vacancies”
            or “Average offered hourly wage”
        • UOM “Unit of Measure”
        • UOM_ID “Unit of Measure ID”
        • SCALAR_FACTOR describes the measurement type – for this data always units
        • SCALAR_ID ID for scalar factor
        • VECTOR StatsCan vector code
        • COORDINATE StatsCan cube coordinate
        • VALUE the value that is being reported in fixed decimal notation (see “DECIMALS”
            below)
        • STATUS encoded according to the meta data file
        • SYMBOL always blank for this data
        • TERMINATED always blank for this data
        • DECIMALS number of decimals to use when interpreting the value (multiply the
            VALUE by 10e-{DECIMALS} to get a true floating point value)


     Commandline Parameters: 1
        argv[0] = this python program   
        argv[1] = name of the input file containing the data

     References
       Data files from https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032805
'''
# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# The 'csv' module gives us access to a tool that will read CSV
# (Comma Separated Value) files and provide us access to each of
# the fields on each line in turn
import csv

def main (argv):
    '''
    Main function in the script. Putting the body of the
    script into a function allows us to separate the local
    variables of this function from the global constants
    declared outside.
    '''

    #   Check that we have been given the right number of parameters,
    #   and store the single command line argument in a variable with
    #   a better name
    if len(argv) != 2:
        print("usage: pre_process_question3.py <file name>")

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)
    
    file_handle = argv[1]      



    # Open the name data input file.  The encoding argument
    # indicates that we want to handle the BOM (if present)
    # by simply ignoring it.

    try:
        file_data = open(file_handle, encoding="utf-8-sig")
    
    except IOError as err:

        # Here we are using the python format() function.
        # The arguments passed to format() are placed into
        # the string it is called on in the order in which
        # they are given.
        print("Unable to open names file '{}' : {}".format(
                file_handle, err), file=sys.stderr)
        sys.exit(1)

    # Create a CSV (Comma Separated Value) reader based on this
    # open file handle.  We can use the reader in a loop iteration
    # in order to access each line in turn.
    file_reader = csv.reader(file_data)
   
    # initialize the count variable to 0
    count = 0

    #   Parse each line of data from the CSV reader, which will break
    #   the lines into fields based on the comma delimiter.
    for i in file_reader:
        # if the count is 0, print the headers of the table and increment the count so that it does not print again
        if count < 1:
            print(i[0],i[1],i[5],i[12], sep = ",")
            count += 1
        # if the occupation is "Software engineers and designers [2173]" and the job vacancy is "Job vacancies"
        # print the data make sure to use > in command line to save the data to a file
        if (i[3] == "Software engineers and designers [2173]" and i[5]=="Average offered hourly wage"):
            if (i[12] == ""):
                print(i[0],i[1],i[5],"0", sep = ",")
            else:
                print(i[0],i[1],i[5],i[12], sep = ",")
    file_data.close()
                

main(sys.argv)