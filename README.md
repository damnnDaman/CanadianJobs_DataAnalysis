# Milestone Project

## Overview

This project processes and analyzes job vacancy data from Statistics Canada. The project includes several Python scripts that pre-process the data and a final script that allows users to interactively refine and visualize the data.

## Project Structure

## Pre-processing Scripts

Before running the final milestone script, you need to run the pre-processing scripts to filter and prepare the data.

### Pre-process Question 1

Filters data for "Software engineers and designers [2173]" and "Average offered hourly wage".

``` python3 pre_process_question1.py "14100328.csv" > "pre_process_question1.csv" ```

### Pre-process Question 2

Filters data for job vacancies specifying non-university certificates or diplomas as the required education level.

```python3 pre_process_Q2_updated.py "14100328.csv" > "extract_Q2.csv"```

### Pre-process Question 3

Filters data for "Software engineers and designers [2173]" and "Job vacancies".

```python3 pre_process_question3.py "14100328.csv" > "pre_process_question3.csv"```

### Pre-process Question 4

Filters data by type of education and "Job vacancies".

```python3 pre_process_question4.py "14100328.csv" > "pre_process_question4.csv" ```

## Final Milestone Script
The final script allows users to interactively refine and visualize the data.

## Running the Script
```python3 MileStone_Final.py```

## Functional Summary
The script will take pre-processed data from Statistics Canada and ask the user to choose variables to better refine the data. The program will then display the data in a table and ask the user if they would like to display the data in a graph.

## Commandline Parameters
 - argv[0]: This Python program

## References
- Data files from Statistics Canada

# Authors
- Jacob Good (1300566)
- Daman Kumar (1306900)
- Hamza Irshad (1261380)
- Ryan Sass-Gregoire (1230473)
