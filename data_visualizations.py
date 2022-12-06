from matplotlib import pyplot as plt
import random
import pandas as pd

class data_visualizations:
    
    def __init__(self, col1, col2=[0]):
        self.col1 = col1
        self.col2 = col2
    
    def compare_variables(self):
        
        
        try:
            fig, ax = plt.subplots(1, figsize=(20,10))
            '''
            Need to figure out how to get the title of the column from the colum info itself, so as to
            limit the amount of parameters the user needs to input when initiating a class.
            ''' 
            # ax.set(xlabel = self.var1_title, ylabel = self.var2_title, title = self.var1_title + ' vs. ' + self.var2_title)
            ax.scatter(self.col1, self.col2, alpha = 0.4, c="blue")
        except ValueError:
            print("In order to compare two variables about a song, you need to input two variables.")
