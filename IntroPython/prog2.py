#!/usr/bin/env python 
#Program prints the size of two DNA fragments after EcoRI cut 
myDNA1 = 'ACAGATGTGCAGACTTTACCGAATTCGCGCTATAGATCGATCGTGTATATGGGCCCACATGAG'
len_fragment1 = myDNA1.find("GAATTC") + 1
len_remfragment = len(myDNA1) - len_fragment1
print"length of the first fragment = ", len_fragment1
print"length of the second fragment = ", len_remfragment

