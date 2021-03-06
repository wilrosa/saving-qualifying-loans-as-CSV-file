# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skips the CSV Header
        next(csvreader)

        # Reads the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, data, header = None):

    # Creates a Path to a new CSV file
    print("Writing the data to a CSV file...")

    # Opens the output CSV file path using `with open`
    with open(csvpath, "w") as csvfile:
                    
        # Creates a csvwriter
        csvwriter = csv.writer(csvfile, delimiter=",")

        # Writes the header to the CSV file
        if header:    
            csvwriter.writerow(header)
        
        # saves as a row in the CSV file.
        csvwriter.writerows(data)