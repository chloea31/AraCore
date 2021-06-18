#! /usr/bin/python3
#-*-coding: utf-8-*-

def add_rxn(name, D_mets, model, rev=True): # this function would be defined to add reactions to the model
    r_name = name
    r_obj = cobra.Reaction(rname)
    r_obj.name = r_name
    r_obj.id = r_name
    model.add_reaction(r_obj)
    r_obj.add_metabolites(D_mets)
    r_obj.objective_coefficient = 0
    if rev:
        r_obj.bounds = (-inf,inf) 
    else:
        r_obj.bounds = (0,inf)

def set_fixed_flux(r_id, val, model): # function probably defined to define fixed flux => consider reactions and bounds
    r_obj = model.reactions.get_by_id(r_id) # search the reaction by id in the model (get_by_id)
    r_obj.bounds = (val,val) # fix the limits of the reaction, which are the same for both the inferior and the superior limits
    # => Fixed limits
    
def set_bounds(r_id, val_tuple, model): # function defined to define bounds for reactions ; retrieve the reaction from its id
    r_obj = model.reactions.get_by_id(r_id) # creation of a summary
    r_obj.bounds = val_tuple # assign bounds (= superior and inferior limits of the reaction)
    
def set_fixed_flux_ratio(r_dict, model): # function defined to fix flux ratio 
    if len(r_dict) == 2:
        r_id1 = list(r_dict.keys())[0]
        r_obj1 = model.reactions.get_by_id(r_id1)
        r_v1 = list(r_dict.values())[0]
        r_id2 = list(r_dict.keys())[1]
        r_obj2 = model.reactions.get_by_id(r_id2)
        r_v2 = list(r_dict.values())[1]
        const = model.problem.Constraint(r_v1 * r_obj2.flux_expression - r_v2 * r_obj1.flux_expression, lb = 0, ub = 0)
        model.add_cons_vars(const)
        return const
