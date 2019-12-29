# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 19:17:24 2019

@author: mh iyer

# visualize the iris dataset with plotnine
# plotnine is a ggplot library for python
"""


 
import pandas as pd
from plotnine import *

if __name__ == "__main__":
    
    # read csv
    path = r'iris.csv'
    
    # get pandas dataframe
    data = pd.read_csv(path)
    
    # visualize data using plotnine
    g = ggplot(data, aes(y = 'sepal_length', x = 'sepal_width', color = 'species')) +    geom_point(shape='o',fill='none', stroke=1,size=4) 
    g = g + ggtitle("Iris Sepal Length vs Iris Sepal Width")  
    print(g)        
