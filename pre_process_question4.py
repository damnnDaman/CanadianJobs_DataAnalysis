#!/usr/bin/env python

#command line example $python3 pre_process_question4.py "14100328.csv" > "pre_process_question4.csv"
'''
pre_process_question4.py
  Author(s): Jacob Good (1300566), Ryan Sass-Gregoire(1230473)
  Earlier contributors(s): Daman Kumar (1306900), Jacob Good (1300566), Ryan Sass-Gregoire(1230473), Hamza Irshad (1261380)

  Project: Milestone IV Pre Process Data For Question 4
  Date of Last Update: Apr 2, 2024.

  Functional Summary
      pre_process_question4.py takes in a CSV (comma separated version) file. Then filters the data of 
      type of education, that further refer to “Job vacancies”.

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
        print("usage: pre_process_question3.py <file name>" )

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
    Alleducation = "Minimum level of education required" #has comma
    educationOne = "No minimum level of education required"
    educationTwo = "High school diploma or equivalent"
    educationThree = "Non-university certificate or diploma"
    educationFour = "Trade certificate or diploma" #has comma
    educationFive = "College" #has comma
    educationSix = "University certificate or diploma below bachelor's level"
    educationSeven = "Bachelor's degree"
    educationEight = "University certificate" #has comma
    educationNine = "Certification requirement" #has comma

    #   Parse each line of data from the CSV reader, which will break
    #   the lines into fields based on the comma delimiter.
    for i in file_reader:
        # if the count is 0, print the headers of the table and increment the count so that it does not print again
        if count < 1:
            print(i[0],i[1],i[3],i[4],i[12], sep = ",")
            count += 1
         # checks if the year is the same as the previous year, if so adds the value to the total
        else:
            # i[0][:4] check the first four digits of the year this way we can add all the quarters together to get the overall year.
                # Type of work is stored with a comma so its a different field than the other types of work
            if (i[4] == Alleducation and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationOne and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationTwo and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationThree and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationFour and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationFive and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationSix and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationSeven and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationEight and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
            elif(i[4] == educationNine and i[5] == "Job vacancies"):
                if (i[12] != ""):
                    print(i[0],i[1],i[3],i[4],i[5],i[12], sep = ",")
    file_data.close()
                

main(sys.argv)