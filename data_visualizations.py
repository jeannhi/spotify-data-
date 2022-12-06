from matplotlib import pyplot as plt
import random
import pandas as pd

class data_visualizations:
    
    def __init__(self, col1, col1_name, col2=[0], col2_name='0'):
        self.col1 = col1
        self.col2 = col2
        self.col1_name = col1_name
        self.col2_name = col2_name
    
    def compare_variables(self):
        
        
        try:
            fig, ax = plt.subplots(1, figsize=(20,10))
            ax.set(xlabel = self.col1_name, ylabel = self.col2_name, title = self.col1_name + ' vs. ' + self.col2_name)
            ax.scatter(self.col1, self.col2, alpha = 0.4, c="blue")
        except ValueError:
            print("In order to compare two variables about a song, you need to input two variables.")
