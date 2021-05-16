# WP2 : Apply Community standards (AraCore_update / FattyCBM_update)


Here, we have a description of the methods used to apply community standards in two metabolic models : AraCore and FattyCBM. These standards, named MIRIAM, SBML and MEMOTE, enable accurate data reuse and reproducibility of the results. 


## I/ Building GPRs (Gene-Protein-Reactions)


-> Define gene-protein-reaction (COBRApy) ? 
[Documentation COBRApy](https://cobrapy.readthedocs.io/en/latest/)


## II/ Building GEMs (Genome-scale Metabolic Models)


- ModelSEED : Integration of metabolic annotations and the reconstruction, comparison and analysis of models 
[Article ModelSEED](https://academic.oup.com/nar/article/49/D1/D1555/5976830)
- BIGG Models : 
    - the model can easily be compared to the set of existing models that are already in this knowledge base. 
    - The BiGG Models resource is compatible with other tools such as COBRApy and Escher (for later)
[Article BIGG Model](https://academic.oup.com/nar/article/44/D1/D515/2502593)

=> Using BiGG Models as a guide for new reconstructions will mean that the new reconstruction is compatible with these tools for modeling and visualization
BiGG Models can be extended to include models built in other research groups, as long as they conform to the standards set out with BiGG Models.
=> Maybe we could use BIGG Models ? -> Rather ModelSEED : we could integrate to use identifiers from ModelSEED database, because it’s a better resource for plant metabolic models and would provide a better compatibility with those - if this isn't giving problems with the BIGG, otherwise, we could provide links to the ModelSeed Ids as part of the extended annotation with this identifiers.org url system.

**Pipeline / Method :** 

> 1st step : Parse the file in Python => extract the information you need (metabolites, reactions and maybe genes).
>
> 2nd step : Introduce more annotations in metabolites, reactions and maybe genes => standards ( = MEMOTE, MIRIAM, SBML).
>
> 3rd step : Convert the Python file into SBML one.
>
> 4th step : Verify if the new/updated model corresponds to the standards (see if we perform this step after converting the Python file into a SBML one).


### 1) De novo reconstruction  

**Metabolites, reactions and genes + databases (UniProt, NCBI, ModelSEED for the integration of metabolic annotations) + parsing of the file in Python**

- Evaluate with MEMOTE (Metabolic Model Test) : -> to assess GEM quality, optimize GEM reproducibility and reuse -> cf fig1 of the article 

    - MEMOTE : 
        - requires SBML3FBC -> this package adds structured, description for model components such as flux bounds, objective functions, GPR rules, metabolite chemical formulas, charges and annotations. 
        - provides quality control and continuous quality assurance of metabolic models 
        - verify the presence of : reactions, metabolites, compartments and genes + metabolite formula and charge information, and GPR rules
        - accepts stoichiometric models encoded in SBML3FBC and previous versions as input
        - benchmarks metabolic models using consensus tests from four general areas : annotation (MIRIAM), basic tests, biomass reaction and stoichiometry 
        - Identify stoichiometric inconsistency, erroneously produced energy metabolites and permanently blocked reactions.
        - enables a comparison between several models
        - can be configured to recognize specific data types as input to predefined experimental tests for model validation
        - validation of MEMOTE using models from 7 GEM collections (GEM reconstructions)
        - we could report any errors to enable community improvement of models as resources
        - MEMOTE tests cover semantic and conceptual requirements, which are fundamental to SBML3FBC and constraint-based modeling respectively; they are extensible to allow the validation of a model’s performance against experimental data and can be executed or integrated into existing pipelines.
[Article MEMOTE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7082222/)

- Save as SBML : -> ensure proper representation of the organism’s biology

    - SBML : 
        - = Systems Biology Markup Language 
        - XML-based standard format
        - for distributing models which have support for COBRA methods through the FBC extension version 2
        - XML script
        - level 3, version 1 required
[SBML website](http://sbml.org/Main_Page)

- Follow MIRIAM guidelines

    - MIRIAM :
        - = Minimum Information Required in the Annotation of Models Registry
        - provides unique, perennial and local-independent identifiers for data used in the biomedical domain
        - MIRIAM Identifiers + MIRIAM Registry
        - properties of MIRIAM Identifiers : unique, unambiguous, perennial, standard compliant, resolvable, free to use
        - properties of MIRIAM Registry : written in Java, makes use of the MVC design pattern, information stored in a MySQL database
        tagging system
[Article MIRIAM](https://academic.oup.com/nar/article/40/D1/D580/2903100)

=> Existing standards + document genome, annotation pipeline, database version
=> Store with README file


### 2) Curation 

- Document all automated and manual curation
- Document all modifications in the reference field with proper citations providing evidence for model decisions


### 3) Simulation


## III/ Implementation of standards


### 1) Loading genomes and GEMs

- Initialize a database in PostgreSQL
- For each genome annotation, load the genes into the database with all the identifiers and external database references
- Load the GEMs into database by reaction, metabolite and gene; separate general information about biological components from model-specific information

### 2) Define BIGG identifiers : provide a single source of correct BIGG IDs that are easy to discover and use in other applications (R_ for reactions, M_ for metabolites)

### 3) ModelPolisher : see GitHub link -> build ModelPolisher (gradle version >= 5.0), then run it (use of docker containers)

### 4) Design and implementation : BIGG Models build with PostgreSQL; BIGG Models is a modular application composed of : 
- a relational database
- a web API ; API = Application Programming Interface = set of definitions and protocols which facilitate the creation and the integration of application softwares; allow the communication of your product with other products and services 
- a website 

### 5) ModelSEED : Integration of metabolic annotations and the reconstruction, comparison and analysis of models ?

[Article Community standards (Carey et al, 2020)](https://www.embopress.org/doi/full/10.15252/msb.20199235)
