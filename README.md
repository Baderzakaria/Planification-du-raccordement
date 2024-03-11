# Planification du raccordement

# authors:
Badreldin zakaria
Nidhal manaa
<details>
<summary><strong>Data Cleaning 👨‍🔧</strong></summary>
  
The `load_and_clean_network_data()` function reads a CSV file containing network data, removes duplicate entries, and filters out rows where infrastructure type is 'infra_intacte'. This ensures that only relevant data is used for further processing.
</details>

<details>
<summary><strong>Infrastructure Object Creation 🛠️</strong></summary>

The `create_infrastructure_dict()` function processes the cleaned network data and creates a dictionary of infrastructure objects. Each object represents a specific infrastructure within the network. The dictionary is indexed by the IDs of the infrastructures.
</details>

<details>
<summary><strong>Building Object Creation 🏢</strong></summary>

The `create_building_list()` function extracts building data from the network and assigns infrastructure objects to each building. It returns a list of building objects, each containing a list of infrastructures it contains.
</details>

<details>
<summary><strong>Repair Planning 📅</strong></summary>

The `plan_repairs()` function takes a list of buildings as input, sorts them based on repair priority, and initiates repairs on the contained infrastructures. The output is a sorted list of buildings indicating the repair sequence.
</details>

<details>
<summary><strong>Priority List Generation 📋</strong></summary>

The `generate_priority_list()` function generates two lists:
1. A priority list, which assigns priority numbers to each building based on their repair sequence.
2. A list of building IDs, providing identifiers for each building.
</details>

<details>
<summary><strong>Conclusion 🏁</strong></summary>

By combining data cleaning, object creation, and repair planning, this project facilitates efficient infrastructure repair scheduling within a network, ensuring optimal resource utilization and timely maintenance.
</details>
