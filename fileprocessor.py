# -*- coding: utf-8 -*-
"""
The following classes and functions are defined in this module;

Reader:
The read function is defined in this class.

read:
This function reads a csv file.

Writer:
The write function is defined in this class.

write:
This function writes a list to a csv file.
"""

# Import modules to work with
import csv

class Reader:
    def read(file_name, number_of_columns):
        """
        This imports a space delimited csv file and reads it into a 
        2D list named snow. 
        
        Variables:
        file_name -- it is a keyword argument for the file to be read.
        number_of_columns -- it is a keyword argument for the 
        number_of _columns label.
        """
        snow = []
        with open(file_name, newline='') as f:
            dataset = csv.reader(f, delimiter = ' ', quoting=csv.QUOTE_NONNUMERIC)
            for row in dataset:
                rowlist = []
                for value in row [:number_of_columns]:
                    rowlist.append(value)
                snow.append(rowlist)
            return snow


class Writer:
    def write(output_file, data_list):
        """
        This creates a space delimited maximum slope dataset file of 
        the snow dataset.
        
        Variables:
        output_file -- it is a keyword argument for the name the file 
        will be saved as.
        data_list -- it is a keyword argument for the data list to be 
        written to a csv file.
        """
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer (f, delimiter = ' ')
            for row in data_list:
                # List of values
                writer.writerow(row)
