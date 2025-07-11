import pubchempy as pcp

# Ask the user for a compound name
name = input("Enter compound name: ")

# Fetch compound data using the name the user entered
compounds = pcp.get_compounds(name, 'name')

# Check if we got any results
if compounds:
    compound = compounds[0]

    print("Molecular Formula:", compound.molecular_formula)
    print("Molecular Weight:", compound.molecular_weight)
    print("IUPAC Name:", compound.iupac_name)
    print(f"SMILES (isomeric):  {compound.isomeric_smiles}")
else:
    print("No compound found. Please check the name and try again.")
