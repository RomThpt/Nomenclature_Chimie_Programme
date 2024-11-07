# Chemical Nomenclature Helper

This **Chemical Nomenclature Helper** is a Python tool designed to assist students with organic chemical nomenclature. Developed in first-year secondary education (1ère), it helps users construct the correct names for hydrocarbons, alcohols, ketones, carboxylic acids, and aldehydes based on their chemical structure.

## 📖 Overview

The main function, `nomenclature`, generates the systematic name of a given organic compound by:
1. **Identifying** the number of carbons in the main chain.
2. **Classifying** functional groups (hydroxyl, carboxyl, carbonyl) to determine the compound's family.
3. **Constructing** the compound's IUPAC name with the appropriate prefixes, radicals, and suffixes.

This tool is a helpful reference and practice aid for students learning organic chemistry basics.

## 📜 Function Details

```python
def nomenclature(c, nb_alcan, place_alcan, grp_car, place_grp):
    # Function description here
```

### Parameters

- **_c_**: Number of carbons in the main chain (integer).
- **_nb_alcan_**: Number of alkyl groups attached to the main chain (integer).
- **_place_alcan_**: Position of the alkyl group on the main chain (integer).
- **_grp_car_**: The functional group of the compound (string, e.g., “OH” for alcohols).
- **_place_grp_**: Position of the functional group (integer).

### Output

Generates and prints the IUPAC name of the compound, including:

- **Radical**: The main chain name based on the number of carbons (e.g., “methan,” “ethan”).
- **Prefix**: Specifies attached alkyl groups (e.g., “methyl,” “ethyl”).
- **Suffix**: Defines the compound family (e.g., “ol” for alcohols, “one” for ketones).

## 🚀 Features

- Hydrocarbons: Names compounds with 1–8 carbons.
- Functional Groups: Supports common organic families:
- Hydroxyl (OH) for alcohols
- Carboxyl (COOH) for carboxylic acids
- Carbonyl (CO) for ketones
- Aldehyde (CHO) for aldehydes
- Positioning: Identifies where alkyl groups and functional groups are located on the main chain.

## 🧩 Example Usage

_Example:
Naming a compound with 3 carbons, an alkyl group, and an alcohol group at specified positions
nomenclature(3, 1, 2, "OH", 1)_

_Output:
Grp hydroxyle et fam alcool
methyl-2-propan-1-ol_

## 💻 Installation

1.	Clone the Repository
```console
git clone https://github.com/yourusername/chemical-nomenclature-helper.git
```

2.	Run the Script
Make sure you have Python installed, then run:
```console
python nomenclature_helper.py
```


## 🛠 Future Enhancements

- Add support for more complex organic compounds.
- Implement quizzes for practice with different compound families.
- Expand to include cyclic and aromatic hydrocarbons.

## 🤝 Contributing

Contributions are welcome!

1.	Fork the repository
2.	Create a new branch (git checkout -b feature/YourFeature)
3.	Commit your changes (git commit -m 'Add YourFeature')
4.	Push to the branch (git push origin feature/YourFeature)
5.	Open a Pull Request

### Happy learning and exploring chemistry!
