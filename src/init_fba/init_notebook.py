#! /usr/bin/python3
#-*-coding: utf-8-*-

from init_fba import pd
from init_fba import os
from init_fba import init_notebook_mode # to display the plots inside the notebook => works with init_notebook_mode(connected=True) 

def init_notebook(theNotebook):
    
    #pandas
    pd.set_option('display.max_columns', 1000) # set_option() sets the value of the specified option
    pd.set_option('display.width', 10000)
    pd.options.display.max_colwidth = 500
    pd.set_option('display.max_rows', 1000)
    
    #init notebook mode for plotly
    init_notebook_mode(connected=True) # to display the plot inside the notebook
    
    #create folder to store results
    directory = theNotebook # path until the directory
    cwd = os.getcwd() # returns current working directory of the process
    if not os.path.exists(theNotebook): 
    # Return True if path refers to an existing path or an open file descriptor. Returns False for broken symbolic links
        os.makedirs(theNotebook) # method in Python used to create a directory recursively. That means while making leaf directory if any intermediate-level directory is missing, os.makedirs() method will create them all.
    if not os.path.exists(theNotebook+'/excel'):
        os.makedirs(theNotebook+'/excel')
    if not os.path.exists(theNotebook+'/figures'):
        os.makedirs(theNotebook+'/figures')
    if not os.path.exists(theNotebook+'/json'):
        os.makedirs(theNotebook+'/json')

# => This function would create the folders needed to display the plots in the notebook. First, the value of the specified option would be 
# defined. The option could be related to the format of the plot
# Secondly, we would precise that we would like to display the plot inside the notebook
# Third, we would create folder to store results. If intermediate folder(s) is/are missing/do(es) not exitst, they would be created.
        