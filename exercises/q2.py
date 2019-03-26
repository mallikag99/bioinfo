def percent_protein(protein, amino):
    protein1 = protein.upper()
    lp = len(protein1)
    amino1 = amino.upper()
    amino_count = protein1.count(amino1)
    percent = amino_count * 100/ lp
    return percent
assert percent_protein("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert percent_protein("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert percent_protein("msrslllrfllfllllpplp", "L") == 50
assert percent_protein("MSRSLLLRFLLFLLLLPPLP", "Y") == 0
~                                                             
