#! /usr/bin/python3
#-*-coding: utf-8-*-

from init_fba import cobra

def load_sbml_model():
    sbml_file = '../models/2018-23-05-mb-genC3.sbml'
    global c3_model
    c3_model = cobra.io.read_sbml_model(sbml_file) # cobra.io.sbml3.read_sbml_model(sbml_file)
    return c3_model

# load and read the SBML file with COBRA
