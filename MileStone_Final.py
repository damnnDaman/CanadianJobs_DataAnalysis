#!/usr/bin/env python

#command line example $python3 MileStone_Final.py

'''
MileStone.py
  Author(s): Jacob Good (1300566), Daman Kumar (1306900), Hamza Irshad (1261380), Ryan Sass-Gregoire (1230473)

  Project: Milestone IV
  Date of Last Update: Apr 2, 2024.

  Functional Summary
      MileStone_Final.py will take pre_processed data from statcitics canada and 
      ask the user to choose varibles to better refine the data. The program will
      then display the data in a table and ask the user if they would like to display
      the data in a graph. 

     Commandline Parameters: 0
        argv[0] = this python program   

     References
       Data files from https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410032805
'''
# The 'sys' module gives us access to system tools, including the
# command line parameters, as well as standard input, output and error
import sys

# matplotlib is for plotting.  The matplotlib
# library is the actual graphics library.
import matplotlib.pyplot as plt 

# The 'csv' module gives us access to a tool that will read CSV
# (Comma Separated Value) files and provide us access to each of
# the fields on each line in turn
import csv

# The 'pandas' module gives us access to a powerful data manipulation
# library.  We can use it to read data from a CSV file and manipulate
# it in various ways.
import seaborn as sns

# The 'pandas' module gives us access to a powerful data manipulation
# library.  We can use it to read data from a CSV file and manipulate
# it in various ways.
import pandas as pd

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
    if len(argv) != 1:
        print("usage: MileStone.py" )

        # we exit with a zero when everything goes well, so we choose
        # a non-zero value for exit in case of an error
        sys.exit(1)

    # creating global variables for all questions
    userInput = 1
    plotFigure = {}
    plotFigureCount = 0
    # just a note to make sure the client knows the data must be pre-processed before running the program
    print("Data must be pre-processed before running the program.")

    # loop to keep the program running until the user decides to exit
    while userInput != 0:

        # main menu
        print("Tasks to display Job Vacancies in Canada")
        print("1. Total offered hourly wage for a particular season")
        print("2. Demand for non-university certificates or diplomas by sector and geographical location")
        print("3. Most vacant jobs by type of work and position")
        print("4. Job vacancies by education level")
        print("0. Exit")
        userInput = int(input())

        # QUESTION 1: Total offered hourly wage for a particular season
        if userInput == 1:
            # assigns the "command line arguments" to variables
            file_handle = "pre_process_question1.csv"      
            geography = "Ontario"
            ref = 1
            # initializes the variables used in loops
            Wvalue = 0.0
            count = 0
            year = 2015
            xAxis=[]    
            yAxis =[]  
            # increasing the index of the array to store plots
            plotFigureCount = plotFigureCount + 1
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

            # getting the first parameter for the quesiton
            print("Provinces: ")
            print("1. Newfoundland and Labrador")
            print("2. Prince Edward Island")
            print("3. Nova Scotia")
            print("4. New Brunswick")
            print("5. Quebec")
            print("6. Ontario")
            print("7. Manitoba")
            print("8. Saskatchewan")
            print("9. Alberta")
            print("10. British Columbia")
            print("11. Yukon")
            print("12. Northwest Territories")
            print("13. Nunavut")
            geography = int(input())
            if geography == 1:
                geography = "Newfoundland and Labrador"
            elif geography == 2:
                geography = "Prince Edward Island"
            elif geography == 3:
                geography = "Nova Scotia"
            elif geography == 4:
                geography = "New Brunswick"
            elif geography == 5:
                geography = "Quebec"
            elif geography == 6:
                geography = "Ontario"
            elif geography == 7:
                geography = "Manitoba"
            elif geography == 8:
                geography = "Saskatchewan"
            elif geography == 9:
                geography = "Alberta"
            elif geography == 10:
                geography = "British Columbia"
            elif geography == 11:
                geography = "Yukon"
            elif geography == 12:
                geography = "Northwest Territories"
            elif geography == 13:
                geography = "Nunavut"

            # getting the second parameter for the question
            print("Season: ")
            print("1. Spring")
            print("2. Summer")
            print("3. Fall")
            print("4. Winter")
            ref = int(input())
            if ref == 1:
                ref = "01"
            elif ref == 2:
                ref = "04"
            elif ref == 3:
                ref = "07"
            elif ref == 4:
                ref = "10"
            # Create a CSV (Comma Separated Value) reader based on this
            # open file handle.  We can use the reader in a loop iteration
            # in order to access each line in turn.
            file_reader = csv.reader(file_data)
            #   Parse each line of data from the CSV reader, which will break
            #   the lines into fields based on the comma delimiter.
            for i in file_reader:
                # prints the header of the file and then increments the count so that it doesn't print again
                if count < 1:
                    print(i[0],i[1],i[2],i[3], sep = ",")
                    count += 1 
                # checks if the year is the same as the previous year, if so adds the value to the total
                else:           
                    # i[0][:4] check the first four digits of the year this way we can add all the quarters together to get the overall year.
                        if (int(i[0][:4]) == year):          
                            if (i[2] == "Average offered hourly wage" and (i[0][5:] == ref) and i[1] == geography):    
                                Wvalue = Wvalue + float(i[3])   
                        # checks if the year is the next year, if so prints the total and then resets the total and increments the year
                        elif (int(i[0][:4]) == (year + 1)):
                            print(year , geography, "Total Wage",int(Wvalue) , sep=",")
                            # appends the values to the x and y axis for the graphs
                            xAxis.append(year) 
                            yAxis.append(Wvalue)   
                            # resets the total
                            Wvalue = 0.0
                            if (i[2] == "Average offered hourly wage"  and (i[0][5:] ==  ref) and i[1] == geography):
                                Wvalue = Wvalue + float(i[3])
                            year = year + 1
            # asks the user if they would like to dispaly the graph
            print("would you like to graph the data? (y/n)")
            graph = input()
            # asks the user if they would like to dispaly the graph and what type of graph they would like to display
            if graph == "y":
                print("1. Bar chart")
                print("2. pie chart")
                print("3. line chart")
                print("Enter your choice:")
                choice = int(input())
                # appends the plot array with the current built plot
                plotFigure[plotFigureCount] = plt.figure(plotFigureCount)
                
                # plots the data to a bar graph
                if (choice == 1):
                    plt.bar(xAxis, yAxis, color = 'blue', width = 0.35, label = "Total wage")#, edgecolor = 'black', linewidth =1.2)
                    plt.xlabel('Year')#, fontsize = 15, color = 'red', fontfamily = 'Times New Roman') 
                    plt.ylabel('Total Wage')#, fontsize = 15, color = 'red', fontfamily = 'Times New Roman') 
                    if(ref =="01"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Spring \n')#, color = 'blue', fontsize = 12)
                    elif(ref =="04"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Summer\n')#, color = 'blue', fontsize = 12)
                    elif(ref =="07"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Fall\n')#, color = 'blue', fontsize = 12)
                    elif(ref =="10"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Winter\n')#, color = 'blue', fontsize = 12)
                    plt.legend()#loc='upper left', shadow=True, fontsize="small")
                    #plt.annotate('Max Value', xy=(5, 50), xytext=(4.5, 45),arrowprops=dict(facecolor='black', shrink=0.05))
                    plotFigure[plotFigureCount].show()
               
                # plots the data to a pie chart
                elif (choice == 2):
                    data_frame = pd.DataFrame({"Year" :xAxis, "Total Wage": yAxis})
                    if(ref =="01"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Spring\n')#, color = 'blue', fontsize = 12)
                    elif(ref =="04"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Summer\n')#, color = 'blue', fontsize = 12)
                    elif(ref =="07"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Fall\n')#, color = 'blue', fontsize = 12)
                    elif(ref =="10"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Winter\n')#, color = 'blue', fontsize = 12)
                    plt.pie(yAxis, labels = xAxis, autopct = '%0.1f%%', radius=0.6)
                    plotFigure[plotFigureCount].show()
                
                # plots the data to a line graph
                elif (choice == 3 ):
                    data_frame = pd.DataFrame({"Year" :xAxis, "Total Wage": yAxis})
                    sns.lineplot(x = 'Year', y = 'Total Wage', data =data_frame)
                    if(ref =="01"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Spring \n')#, color = 'blue', fontsize = 12)
                    elif(ref =="04"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Summer \n')#, color = 'blue', fontsize = 12)
                    elif(ref =="07"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Fall\n')#, color = 'blue', fontsize = 12)
                    elif(ref =="10"):
                        plt.title('Total hourly wage spend on Software engineers\n and designers [2173] in Winter\n')#, color = 'blue', fontsize = 12)
                    plotFigure[plotFigureCount].show()





        # Question 2
        elif userInput == 2:
            # File name that contains pre-processed data
            file_name = "extract_Q2.csv"
            plotFigureCount = plotFigureCount + 1
            # First parameter is location 
            print("Please choose a province:")
            print("Provinces: ")
            print("1. Newfoundland and Labrador")
            print("2. Prince Edward Island")
            print("3. Nova Scotia")
            print("4. New Brunswick")
            print("5. Quebec")
            print("6. Ontario")
            print("7. Manitoba")
            print("8. Saskatchewan")
            print("9. Alberta")
            print("10. British Columbia")
            print("11. Yukon")
            print("12. Northwest Territories")
            print("13. Nunavut")
            location = int(input())
            if location == 1:
                location = "Newfoundland and Labrador".lower()
            elif location == 2:
                location = "Prince Edward Island".lower()
            elif location == 3:
                location = "Nova Scotia".lower()
            elif location == 4:
                location = "New Brunswick".lower()
            elif location == 5:
                location = "Quebec".lower()
            elif location == 6:
                location = "Ontario".lower()
            elif location == 7:
                location = "Manitoba".lower()
            elif location == 8:
                location = "Saskatchewan".lower()
            elif location == 9:
                location = "Alberta".lower()
            elif location == 10:
                location = "British Columbia".lower()
            elif location == 11:
                location = "Yukon".lower()
            elif location == 12:
                location = "Northwest Territories".lower()
            elif location == 13:
                location = "Nunavut".lower()
            # Convert NOC sector parameter to lowercase
            sector_part_of_noc = input("Enter keyword from NOC, such as Software: ").lower()
            
            try:
                # Open the file for reading
                file_data = open(file_name, encoding="utf-8-sig")
                file_reader = csv.reader(file_data)

                # Final processing begins here

                # Adjust headers for updated processing
                updated_headers = [
                    'REF_DATE', 'GEO', 'National Occupational Classification', 'Statistics', 'VALUE'
                ]
                print(','.join(updated_headers))

                # Variables to plot data by year
                current_year = ""
                yearly_sum = 0
                years = []
                job_vacancies = []

                for row in file_reader:
                    # Convert to lower for comparing
                    geo_location = row[1].lower()
                    noc_code = row[2].lower()
                    statistics = row[4].lower()
                    year = row[0][:4]  # Get the year from the REF_DATE

                    # Ensure case insensitive matching and only look for vacancies statistic
                    if location in geo_location and sector_part_of_noc in noc_code and "job vacancies" == statistics:
                        if 'except' not in noc_code:  # Additional check to exclude unwanted matches
                            # Handle commas in NOC
                            if ',' in row[2]:
                                processed_noc = f'"{row[2]}"'
                            else:
                                processed_noc = row[2]

                            # Use original case for printing
                            processed_row = [row[0], row[1], processed_noc, "Job vacancies", row[5] if row[5] else '0']
                            print(','.join(processed_row))

                            # For yearly calculations
                            if not row[5]:
                                job_vacancy = 0
                            else:
                                job_vacancy = int(row[5])

                            if year != current_year:
                                if current_year:  # not the first loop
                                    years.append(current_year)
                                    job_vacancies.append(yearly_sum)
                                    yearly_sum = 0  # Reset for the new year
                                
                                current_year = year

                            yearly_sum += job_vacancy

                # After looping through all rows, append the sum of the last year
                if current_year:
                    years.append(current_year)
                    job_vacancies.append(yearly_sum)

                file_data.close()

            except IOError as err:
                print(f"Error opening file '{file_name}': {err}", file=sys.stderr)
                sys.exit(1)

            # Ask the user if they want to plot the data
            plot_choice = input("Do you want to plot the data? (yes/no): ").lower()
            if plot_choice != 'yes':
                return

            # Choose the type of graph
            graph_type = input("Choose the type of graph (1 for Bar chart, 2 for Line chart): ")
            # appends the plot array with the current built plot
            plotFigure[plotFigureCount] = plt.figure(plotFigureCount)
            # Bar graph
            if graph_type == '1':
                plt.bar(years, job_vacancies, color='blue', label='Job Vacancies')
                plt.xlabel('Date')
                plt.ylabel('Number of Job Vacancies')
                graph_title = f'Job Vacancies in {location.title()} for {sector_part_of_noc.title()}'
            # Line graph
            elif graph_type == '2':
                plt.plot(years, job_vacancies, marker='o', linestyle='-', color='red', label='Job Vacancies')
                plt.xlabel('Date')
                plt.ylabel('Number of Job Vacancies')
                graph_title = f'Trend of Job Vacancies in {location.title()} for {sector_part_of_noc.title()}'
            else:
                print("Invalid graph type selected.")
                return

            plt.title(graph_title)
            plt.xticks(rotation=45)  # Rotate x axis labels for better readability
            plt.legend()
            plotFigure[plotFigureCount].show()
            plt.tight_layout()





              #QUESTION 3: Most vacant jobs by type of work and position
        elif userInput == 3:
            # declaring values and defaults
            Wvalue = 0
            workColour = "lime"
            Pvalue = 0
            positionColour = "lime"
            count = 0
            geography = "Canada"
            # declaring the year as the starting year
            year = 2015
            # increasing the index of the array to store plots
            plotFigureCount = plotFigureCount + 1
            # getting the pre processes data for the question
            file_handle = "pre_process_question3.csv" 
            # setiing the arrays for the bar values
            x = [] 
            y = [] 
            x2 = [] 
            y2 = [] 
            # getting the first parameter for the quesiton
            print("Type of work:")
            print("1. Full-time")
            print("2. Part-time")
            print("3. All-types")
            work = int(input())
            # setting the user input to the correct value
            if work == 1:
                work = "Full-time"
                workColour = "orange"
            elif work == 2:
                work = "Part-time"
                workColour = "red"
            elif work == 3:
                work = "Type of work"
                workColour = "pink"
            # getting the second parameter for the question
            print("Type of position:")
            print("1. Permanent")
            print("2. Temporary")
            print("3. Seasonal")
            print("4. All-types")
            position = int(input())
            # setting the user input to correct value
            if position == 1:
                position = "Permanent"
                positionColour = "turquoise"
            elif position == 2:
                position = "Temporary (seasonal and non-seasonal)"
                positionColour = "purple"
            elif position == 3:
                position = "Seasonal"
                positionColour = "blue"
            elif position == 4:
                position = "Type of position"
                positionColour = "lightblue"
            # getting the first parameter for the quesiton
            print("Provinces: ")
            print("1. Newfoundland and Labrador")
            print("2. Prince Edward Island")
            print("3. Nova Scotia")
            print("4. New Brunswick")
            print("5. Quebec")
            print("6. Ontario")
            print("7. Manitoba")
            print("8. Saskatchewan")
            print("9. Alberta")
            print("10. British Columbia")
            print("11. Yukon")
            print("12. Northwest Territories")
            print("13. Nunavut")
            print("14. All provinces")
            geography = int(input())
            if geography == 1:
                geography = "Newfoundland and Labrador"
            elif geography == 2:
                geography = "Prince Edward Island"
            elif geography == 3:
                geography = "Nova Scotia"
            elif geography == 4:
                geography = "New Brunswick"
            elif geography == 5:
                geography = "Quebec"
            elif geography == 6:
                geography = "Ontario"
            elif geography == 7:
                geography = "Manitoba"
            elif geography == 8:
                geography = "Saskatchewan"
            elif geography == 9:
                geography = "Alberta"
            elif geography == 10:
                geography = "British Columbia"
            elif geography == 11:
                geography = "Yukon"
            elif geography == 12:
                geography = "Northwest Territories"
            elif geography == 13:
                geography = "Nunavut"
            elif geography == 14:
                geography = "Canada"


            # opening the pre processed data
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
            #   Parse each line of data from the CSV reader, which will break
            #   the lines into fields based on the comma delimiter.
            for i in file_reader:
                # prints the header of the file and then increments the count so that it doesn't print again
                if count < 1:
                    print(i[0],i[1],i[3],i[5], sep = ",")
                    count += 1        
                # checks if the year is the same as the previous year, if so adds the value to the total
                else:
                    # i[0][:4] check the first four digits of the year this way we can add all the quarters together to get the overall year.
                    if (int(i[0][:4]) == year):
                        if (i[1] == geography):    
                            # Type of work is stored with a comma so its a different field than the other types of work
                            if (i[3] == "Type of work" and i[3] == work):
                                Wvalue = Wvalue + int(i[6])
                            elif(i[3] == work):
                                Wvalue = Wvalue + int(i[5])
                            # Type of position is stored with a comma so its a different field than the other types of position
                            if (i[3] == "Type of position" and i[3] == position):
                                Pvalue = Pvalue + int(i[6])
                            elif (i[3] == position):
                                Pvalue = Pvalue + int(i[5])
                    # checks if the year is the next year, if so prints the total and then resets the total and increments the year
                    elif (int(i[0][:4]) == (year + 1)):
                        # the temporary value is a long string just cleaning it up to display
                        if position == "Temporary (seasonal and non-seasonal)":
                            print(year,geography,work,Wvalue, sep = ",")
                            print(year,geography,"Temporary",Pvalue, sep = ",")   
                        else:
                            print(year,geography,work,Wvalue, sep = ",")
                            print(year,geography,position,Pvalue, sep = ",")
                        # adds the values to the bar graph for each year
                        x.append(float(year)-0.18)
                        y.append(Wvalue)
                        x2.append(float(year)+0.18)
                        y2.append(Pvalue)
                        # resets the total
                        Wvalue = 0
                        Pvalue = 0
                        #counts the total number of job vacancies before going to the next row
                        if (i[1] == geography):    
                            if (i[3] == "Type of work" and i[3] == work):
                                Wvalue = Wvalue + int(i[6])
                            elif(i[3] == work):
                                Wvalue = Wvalue + int(i[5])
                            if (i[3] == "Type of position" and i[3] == position):
                                Pvalue = Pvalue + int(i[6])
                            elif (i[3] == position):
                                Pvalue = Pvalue + int(i[5])
                        year = year + 1
            # asks the user if they would like to dispaly the graph
            print("would you like to graph the data? (y/n)")
            graph = input()
            # appends the plot array with the current built plot
            plotFigure[plotFigureCount] = plt.figure(plotFigureCount)
            if graph == "y":
                # plots the data to a bar graph
                if position == "Temporary (seasonal and non-seasonal)":
                    plt.bar(x, y, color = workColour, width = 0.36, label = work) 
                    plt.bar(x2, y2, color = positionColour, width = 0.36, label = "Temporary") 
                else:
                    plt.bar(x, y, color = workColour, width = 0.36, label = work) 
                    plt.bar(x2, y2, color = positionColour, width = 0.36, label = position) 
                plt.xlabel('Years') 
                plt.ylabel('Number of Job Vacincies') 
                plt.title('Job Vacancies in %s for Software Engineers and Designers\n by Work and Position over the Years' %geography) 
                plt.legend() 
                # displays the plot from the array 
                plotFigure[plotFigureCount].show()
    

            # closes the file before going back to the main menu
            file_data.close()

            



        elif userInput == 4:
        #Question 4: Displays the data of occupational classification 
        #and how the different levels of education play a role in job 
        #vacancies for total occuptional classifications.
            
        # File name that contains pre-processed data
            file_name = "pre_process_question4.csv"
            plotFigureCount = plotFigureCount + 1

            # Initialize lists to store occupation names and corresponding stats
            occupation = "software"
            geography = "Canada"
            x = []
            x2 = []
            x3 = []
            x4 = []
            y = []
            y2 = []
            y3 = []
            y4 = []
            count = 0
            year = 2015
            Alleducation = "Minimum level of education required" #has comma
            Allvalue = 0
            educationOne = "No minimum level of education required"
            valueOne = 0
            educationTwo = "High school diploma or equivalent"
            valueTwo = 0
            educationThree = "Non-university certificate or diploma"
            valueThree = 0
            educationFour = "Trade certificate or diploma" #has comma
            valueFour = 0
            educationFive = "College" #has comma
            valueFive = 0
            educationSix = "University certificate or diploma below bachelor's level"
            valueSix = 0
            educationSeven = "Bachelor's degree"
            valueSeven = 0
            educationEight = "University certificate" #has comma
            valueEight = 0
            educationNine = "Certification requirement" #has comma
            valueNine = 0
            print("Please choose an occupation: (ex. software, financial)")
            occupation = input().lower()

            # getting the first parameter for the quesiton provice
            print("Provinces: ")
            print("1. Newfoundland and Labrador")
            print("2. Prince Edward Island")
            print("3. Nova Scotia")
            print("4. New Brunswick")
            print("5. Quebec")
            print("6. Ontario")
            print("7. Manitoba")
            print("8. Saskatchewan")
            print("9. Alberta")
            print("10. British Columbia")
            print("11. Yukon")
            print("12. Northwest Territories")
            print("13. Nunavut")
            print("14. All provinces")
            geography = int(input())
            if geography == 1:
                geography = "Newfoundland and Labrador"
            elif geography == 2:
                geography = "Prince Edward Island"
            elif geography == 3:
                geography = "Nova Scotia"
            elif geography == 4:
                geography = "New Brunswick"
            elif geography == 5:
                geography = "Quebec"
            elif geography == 6:
                geography = "Ontario"
            elif geography == 7:
                geography = "Manitoba"
            elif geography == 8:
                geography = "Saskatchewan"
            elif geography == 9:
                geography = "Alberta"
            elif geography == 10:
                geography = "British Columbia"
            elif geography == 11:
                geography = "Yukon"
            elif geography == 12:
                geography = "Northwest Territories"
            elif geography == 13:
                geography = "Nunavut"
            elif geography == 14:
                geography = "Canada"
            # opening the pre processed data
            try:
                file_data = open(file_name, encoding="utf-8-sig")
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

            #reading the data from the file
            for i in file_reader:
                #converts the occupation to lowercase
                noc_code = i[2].lower()
                # if the count is 0, print the headers of the table and increment the count so that it does not print again
                if count < 1:
                    print(i[0],i[1],i[2],i[3],i[4], sep = ",")
                    count += 1
                # checks if the year is the same as the previous year, if so adds the value to the total
                else:
                    # i[0][:4] check the first four digits of the year this way we can add all the quarters together to get the overall year.
                    # checks if the entered occupation is in the noc_code incase the user did not enter the full occupation
                    if (int(i[0][:4]) == year and i[1] == geography and occupation in noc_code):
                        # Type of work is stored with a comma so its a different field than the other types of work
                        if (i[3] == Alleducation):
                            Allvalue = Allvalue + int(i[5])
                        elif(i[3] == educationOne):
                            valueOne = valueOne + int(i[5])
                        elif(i[3] == educationTwo):
                            valueTwo = valueTwo + int(i[5])
                        elif(i[3] == educationThree):
                            valueThree = valueThree + int(i[5])
                        elif(i[3] == educationFour):
                            valueFour = valueFour + int(i[5])
                        elif(i[3] == educationFive):
                            valueFive = valueFive + int(i[5])
                        elif(i[3] == educationSix):
                            valueSix = valueSix + int(i[5])
                        elif(i[3] == educationSeven):
                            valueSeven = valueSeven + int(i[5])
                        elif(i[3] == educationEight):
                            valueEight = valueEight + int(i[5])
                        elif(i[3] == educationNine):
                            valueNine = valueNine + int(i[5])
                    # checks if the year is the next year, if so prints the total and then resets the total and increments the year
                    elif (int(i[0][:4]) == (year + 1) and i[1] == geography and occupation in noc_code):
                        print(year,i[1],i[2],Alleducation,Allvalue, sep = ",")
                        print(year,i[1],i[2],educationOne,valueOne, sep = ",")
                        print(year,i[1],i[2],educationTwo,valueTwo, sep = ",")
                        print(year,i[1],i[2],educationThree,valueThree, sep = ",")
                        print(year,i[1],i[2],educationFour,valueFour, sep = ",")
                        print(year,i[1],i[2],educationFive,valueFive, sep = ",")
                        print(year,i[1],i[2],educationSix,valueSix, sep = ",")
                        print(year,i[1],i[2],educationSeven,valueSeven, sep = ",")
                        print(year,i[1],i[2],educationEight,valueEight, sep = ",")
                        print(year,i[1],i[2],educationNine,valueNine, sep = ",")
                        # appends the values to the x and y axis for the graphs
                        x.append(float(year)-0.26)
                        x2.append(float(year)-0.09)
                        x3.append(float(year)+0.09)
                        x4.append(float(year)+0.26)
                        y.append(valueOne)
                        y2.append(valueThree)
                        y3.append(valueSix)
                        y4.append(valueSeven)
                        Allvalue = 0
                        valueOne = 0
                        valueTwo = 0
                        valueThree = 0
                        valueFour = 0
                        valueFive = 0
                        valueSix = 0
                        valueSeven = 0
                        valueEight = 0
                        valueNine = 0
                        # Type of work is stored with a comma so its a different field than the other types of work
                        if (i[3] == Alleducation):
                            Allvalue = Allvalue + int(i[5])
                        elif(i[3] == educationOne):
                            valueOne = valueOne + int(i[5])
                        elif(i[3] == educationTwo):
                            valueTwo = valueTwo + int(i[5])
                        elif(i[3] == educationThree):
                            valueThree = valueThree + int(i[5])
                        elif(i[3] == educationFour):
                            valueFour = valueFour + int(i[5])
                        elif(i[3] == educationFive):
                            valueFive = valueFive + int(i[5])
                        elif(i[3] == educationSix):
                            valueSix = valueSix + int(i[5])
                        elif(i[3] == educationSeven):
                            valueSeven = valueSeven + int(i[5])
                        elif(i[3] == educationEight):
                            valueEight = valueEight + int(i[5])
                        elif(i[3] == educationNine):
                            valueNine = valueNine + int(i[5])
                        year = year + 1
            file_data.close()
                    
            # asks the user if they would like to dispaly the graph
            print("would you like to graph the data? (y/n)")
            graph = input()
            # appends the plot array with the current built plot
            plotFigure[plotFigureCount] = plt.figure(plotFigureCount)
            if graph == "y":
                # Plot the bar graph
                plt.bar(x, y, color = "lightblue", width = 0.18,label = educationOne) 
                plt.bar(x2, y2, color = "steelblue", width = 0.18, label = educationThree) 
                plt.bar(x3, y3, color = "orange", width = 0.18, label = educationSix) 
                plt.bar(x4, y4, color = "cyan", width = 0.18, label = educationSeven) 
                # Bar graph for stats/occupation
                plt.xlabel('Year')
                plt.ylabel('Job vacancies')
                plt.title('Job vacancies by occupation and Education Levels')
                plt.legend()
                plotFigure[plotFigureCount].show()

# if the user enters 0 the program will exit
main(sys.argv)

    