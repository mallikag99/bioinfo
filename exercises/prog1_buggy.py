#!/usr/bin/env python3
import re
myfile = open("/home/mallika/yeast_proteins.fasta")
protein = ""
def cleanup(seq):
    seq = seq.upper() 
    seq = re.sub(r"[^A-Za-z]","", seq) 
    return seq 
    for line in myfile:
        line = line.rstrip('\n')
        m1 = re.search(r">(.*?) ", line)
        m2 = re.search(r"(.*?)\*", line)
        if m1:
            name = m1.group(1)
        if m2:
            protein = protein + m2.group(1)
            C_count = protein.count('C')
            length = len(protein)
            pct_C = round((C_count/length)*100,2)
            print(name,pct_C,"%")
            protein = ""
        protein = protein + cleanup(line)
myfile.close()

