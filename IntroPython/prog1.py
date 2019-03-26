#!/usr/bin/env python 
# prints out the complement of the given DNA sequence
myDNA1 =  'ACAGATGTGCAGACTTTACCGAATTCGCGCTATAGATCGATCGTGTATATGGGCCCACATGAG'
strand1 = myDNA1.replace("A","t")
strand2 = strand1.replace("C","g")
strand3 = strand2.replace("G","C")
strand4 = strand3.replace("T","A")
compDNA = strand4.upper()
print"Complement of myDNA1 =", compDNA
