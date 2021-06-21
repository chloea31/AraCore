# WORKING WITH PLANT METABOLIC MODELS 


## Table of contents


1. Description
2. Requirements
3. Usage
4. Authors
5. Project status


## Description


**The aim of this internship is to build mapping tables for metabolites, reactions and genes in order to improve the AraCore metabolic model and make it MIRIAM compliant. In addition, the other aim is to perform FBA and make plots via plotly in order to optimize the flow of metabolites through the metabolic network.** 

Concerning the construction of mapping tables, we used Python as programming language and Pandas as API to build a kind of pipeline. 

The pipelines are built as presented in the corresponding notebook and following the steps described in the report. 


## Requirements


**Intall conda:**
[Conda](https://docs.conda.io/projects/conda/en/latest/commands/install.html)

**Create the environment from environment.yml file:**
conda env create -f environment.yml --name aracore_update

**Activate the environment:**
conda activate aracore_update


## Usage


**To run the pipeline:**
Click on "Cell", then "Run all" on top of each notebook.

**After execution the script will output all the information process:**
The results will be printed after execution of each cell.

**Location of the output files:**
In the notebooks, we included the corresponding folder for each mapping table. All of them are stored in [output_files](https://github.com/SeedRecon/AraCore_update/tree/main/data/processed) folder. In this forlder, you will find the mapping tables named according to their content: 
- "metabolite-mapping-table" for the metabolites; 
- "reaction-mapping-table" for the reactions; 
- "gene-mapping-table" for genes; 


## Authors


The members were:
- Supervisor: Dr. Mary-Ann Blätke
- Student: Chloé Aujoulat


## Project status


The project is still running. 