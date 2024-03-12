import infra
import building
import pandas as pd

#data cleaning
def load_and_clean_network_data(filepath):
    """
The load_and_clean_network_data function takes a filepath as an argument and returns a pandas dataframe.
The function reads the csv file at the given path, drops duplicates, and removes rows where infra_type is 'infra_intacte'.
so now we manupilate the data we need

:param filepath: Specify the path to the file that we want to read
:return: A dataframe with all the rows where &quot;infra_type&quot; is not equal to &quot;infra_intacte&quot;
:doc-author: badreldin
"""
    network_df = pd.read_csv(filepath).drop_duplicates()
    return network_df[network_df["infra_type"] != "infra_intacte"]

#assign data to objects
def create_infrastructure_dict(network_df):
    """
The create_infrastructure_dict function takes a dataframe as input and returns a dictionary of infrastructure objects.
The keys of the dictionary are the IDs of each infrastructure, while the values are instances of infra.Infra class.

:param network_df: Create the infrastructure dictionary
:return: A dictionary of infrastructure objects
:doc-author: badreldin
"""
    dict_infras = {}
    for infra_id, infra_data in network_df.groupby(by="infra_id"):
        length = infra_data["longueur"].iloc[0]
        infra_type = infra_data["infra_type"].iloc[0]
        nb_houses = sum(infra_data["nb_maisons"].values)
        dict_infras[infra_id] = infra.Infra(infra_id, length, infra_type, nb_houses)
    return dict_infras

def create_building_list(network_df, dict_infras):
    """
The create_building_list function takes a dataframe and a dictionary as input.
The dataframe contains the information about the buildings, their id and which infrastructures they contain.
The dictionary contains all the infrastructure objects with their id as key.
It returns a list of building objects.

:param network_df: Extract the building data from the network_df
:param dict_infras: Create a list of infrastructures for each building
:return: A list of buildings
:doc-author: badreldin
"""
    list_buildings = []
    for building_id, building_data in network_df.groupby(by="id_batiment"):
        list_infras = [dict_infras[infra_id] for infra_id in building_data["infra_id"].values]
        list_buildings.append(building.Building(building_id, list_infras))
    return list_buildings

   








   
def generate_priority_list(list_buildings):
    """
The generate_priority_list function takes a list of buildings as input and returns two lists:
    1. A priority_list, which is a list of integers that correspond to the index in the original building list.
    2. A building_ids, which is a list of strings that correspond to the id's for each building in order.

:param list_buildings: Generate the priority list
:return: A list of building ids and a priority_list
:doc-author: badreldin
"""
    priority_list = []
    building_ids = []
    for index, building in enumerate(list_buildings):
        priority_list.append(index)
        building_ids.append(building.id_building)
        print(building)
    return priority_list, building_ids

if __name__ == "__main__":
    network_df = load_and_clean_network_data("./reseau_en_arbre.csv")
    dict_infras = create_infrastructure_dict(network_df)
    list_buildings = create_building_list(network_df, dict_infras)
    list_sorted_buildings = plan_repairs(list_buildings)
    priority_list, building_ids = generate_priority_list(list_sorted_buildings)