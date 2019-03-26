#!/usr/bin/env python3
def percent_amino(protein, amino = ['A','I','L','M','F','W','Y','V']):
    protein1 = protein.upper()
    lp = len(protein1)
    result = 0
    for i in amino:
        i_count = protein1.count(i)
        result = result + i_count
    percent = result*100/lp
    return percent

assert percent_amino("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert percent_amino("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert percent_amino("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert percent_amino("MSRSLLLRFLLFLLLLPPLP") == 65
