# -*- coding: utf-8 -*-
"""
The following classes and functions are defined in this module;

Gradient:
This class secures the snow variable.

calculate:
This function calaculates the slope of a cell with respect to its neighbours.

find_maximum_slope:
This function determines the highest slope value that exists for a cell
with respect to its neighbours.
"""


class Gradient():
    def __init__ (self, snow):
        """
        This class secures snow, d1, d2, d3, d4, d5, d6, d7 and d8 
        variables.
        
        Instance variables:
        snow -- it represents the raster grid of heights dataset
        """
        
        self.snow = snow
        self.d1 = 0
        self.d2 = 0
        self.d3 = 0
        self.d4 = 0
        self.d5 = 0
        self.d6 = 0
        self.d7 = 0
        self.d8 = 0
        
        
        
    def calculate(self, i, j):
        """
        This calculates the slope of a cell with respect to each of its 
        eight contiguous neighbours
        """
        
        self.d1 = (self.snow[i][j] - self.snow[i][j+1]) / 1
        self.d2 = (self.snow[i][j] - self.snow[i-1][j+1]) / 2**0.5
        self.d3 = (self.snow[i][j] - self.snow[i-1][j]) / 1
        self.d4 = (self.snow[i][j] - self.snow[i-1][j-1]) / 2**0.5        
        self.d5 = (self.snow[i][j] - self.snow[i][j-1]) / 1        
        self.d6 = (self.snow[i][j] - self.snow[i+1][j-1]) / 2**0.5
        self.d7 = (self.snow[i][j] - self.snow[i+1][j]) / 1
        self.d8 = (self.snow[i][j] - self.snow[i+1][j+1]) / 2**0.5
        
        
        
    def find_maximum_slope(self):
        """
        This determine and returns the maximum slope value calculated 
        in the 'calculate' function above.
        """
        
        slopes = [
            self.d1, self.d2, self.d3, self.d4, 
            self.d5, self.d6, self.d7, self.d8
        ]
        return max(slopes)