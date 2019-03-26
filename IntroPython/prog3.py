#!/usr/bin/env python
#program to print out GC content of the given DNA sequence
from __future__ import division 
myDNA1 = 'ACAGATGTGCAGACTTTACCGAATTCGCGCTATAGATCGATCGTGTATATGGGCCCACATGAG'
length_myDNA1 = len(myDNA1)
Gs = myDNA1.count('G')
Cs = myDNA1.count('C')
gc_content = (Gs + Cs) /length_myDNA1
print"GC content is ", gc_content 
