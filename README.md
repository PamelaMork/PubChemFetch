# PubChemFetch
Fetches small molecules and information from PubChem using pubchempy

Working script. It does not pull SMILES correctly. 

This script does, but getting there with students is more than I want to tackle this early in the course. 

import requests

cid = 5429  # Theobromine CID
url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/JSON"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    props = data["PC_Compounds"][0]["props"]

    formula = weight = ""
    smiles_variants = {}

    for prop in props:
        urn = prop.get("urn", {})
        label = urn.get("label", "")
        name = urn.get("name", "")
        value = prop.get("value", {}).get("sval", "")

        if label == "Molecular Formula":
            formula = value
        elif label == "Molecular Weight":
            weight = value
        elif label == "SMILES":
            smiles_variants[name] = value

    print("Molecular Formula:", formula)
    print("Molecular Weight:", weight)

    if smiles_variants:
        for variant, val in smiles_variants.items():
            print(f"{variant} SMILES:", val)
    else:
        print("SMILES not found")

except requests.exceptions.RequestException as e:
    print("HTTP error:", e)
except Exception as e:
    print("Error parsing data:", e)
