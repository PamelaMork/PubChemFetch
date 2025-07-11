import pubchempy as pcp

# Ask user for a compound name
name = input("Enter the name of a compound: ")

# Fetch compound data
compounds = pcp.get_compounds(name, 'name')

# Check if we got a result
if compounds:
    compound = compounds[0]  # Use the first result

# Define label width
label_width = 20

print("\n🧪 Compound Summary")
print("=" * 40)
print("Name:".ljust(label_width), compound.iupac_name)
print("Formula:".ljust(label_width), compound.molecular_formula)
print("Mol Weight:".ljust(label_width), compound.molecular_weight)
print("Exact Mass:".ljust(label_width), compound.exact_mass)
print("XLogP:".ljust(label_width), compound.xlogp)
print("H-bond Donors:".ljust(label_width), compound.h_bond_donor_count)
print("H-bond Acceptors:".ljust(label_width), compound.h_bond_acceptor_count)
print("Rotatable Bonds:".ljust(label_width), compound.rotatable_bond_count)
print("TPSA:".ljust(label_width), compound.tpsa)
print("InChI Key:".ljust(label_width), compound.inchikey)
print("SMILES:".ljust(label_width), compound.isomeric_smiles)
