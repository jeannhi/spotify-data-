from matplotlib import pyplot as plt
import random
import pandas as pd

class data_visualizations:
    '''
    The following code creates an instance of the data_visualizations class
    
    Variables:
    col1 / col2 -- Columns of the spotify dataframe
    col1_name / col2_name -- Names for the columns to be used in the data visualization
    '''
    def __init__(self, col1, col1_name, col2=[0], col2_name='0'):
        # Assigning Variables
        self.col1 = col1
        self.col2 = col2
        self.col1_name = col1_name
        self.col2_name = col2_name
    
    '''
    The following function outputs a scatterplot with a variable on each axis
    '''
    def compare_variables(self):
        try:
            # Basic information about the plot
            fig, ax = plt.subplots(1, figsize=(20,10))
            # Sets the axis labels and graph title
            ax.set(xlabel = self.col1_name, ylabel = self.col2_name, title = self.col1_name + ' vs. ' + self.col2_name)
            # Creates the scatterplot, deciding opacity and graph color
            ax.scatter(self.col1, self.col2, alpha = 0.4, c="blue")
            
        # Gives the user an error if they try to plot a scatterplot with only one column from the spotify dataframe
        except ValueError:
            print("In order to compare two variables about a song, you need to input two variables.")
