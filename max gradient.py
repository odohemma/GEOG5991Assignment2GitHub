# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 18:31:30 2018

@author: user
"""
# Import modules to work with
import csv
from fileprocessor import Reader, Writer
import matplotlib.pyplot
import gradientframework


# This is the number of rows and columns in the dataset.
# It can be edited to suit your dataset if using a different dataset.
number_of_rows = 300
number_of_columns = 300


# This imports a csv file and reads it into a 2D list named snow.
# The file used here is 'snow.slope.txt'. 
# Replace the filename with the directory of the file you wish to 
# process, or edit only the filename if the file is in the same 
# directory with this code.
snow = Reader.read('snow.slope.txt', number_of_columns)
        
        

# This creates an empty list for maximum gradients to be stored in.
maxgradient = []


# This defines the number of rows and columns for the gradient dataset
gradient_values = number_of_columns - 1
gradient_rows = number_of_rows - 1


gradient = gradientframework.Gradient(snow)


# This calculates slope of all grid cells with respect to cells 
# contiguous to it, and fills the maxgradient list with the maximum 
# slope value of each cell.
for j in (range(1,gradient_rows)):      
    sloperow = []      
    for i in (range(1,gradient_values)):
        
        # This calculates the slope between a grid cell and its eight
        # neighbours (four are adjacent, and four are diagonal).
        gradient.calculate(j, i)
        
        # This determines the maximum slope value between a cell and 
        # its eight neighbours
        gradient.find_maximum_slope()
        
        # This appends the maximum slope value to the sloperow list
        sloperow.append(gradient.find_maximum_slope())

        
    # This appends the sloperow list to the maxgradient list    
    maxgradient.append(sloperow)
    
  
# This plots the topo file
matplotlib.pyplot.imshow(snow)
matplotlib.pyplot.show()

# This plots the maxgradient list
matplotlib.pyplot.imshow(maxgradient)
matplotlib.pyplot.show()


# This creates a maximum slope dataset file of the snow dataset in 
# text format.
# The file created here is 'snow.maxgradient.txt'
Writer.write('snow.maxgradient.txt', maxgradient)