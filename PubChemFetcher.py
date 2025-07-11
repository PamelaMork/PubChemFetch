import pubchempy as pcp

# Fetch compound data for theobromine by name
compounds = pcp.get_compounds('theobromine', 'name')

if compounds:
    compound = compounds[0]  # Use the first match

    print("Molecular Formula:", compound.molecular_formula)
    print("Molecular Weight:", compound.molecular_weight)
    print("SMILES:", compound.canonical_smiles)
else:
    print("Compound not found.")
