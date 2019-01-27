#!/usr/bin/env python 
#program to print out coding sequence and non-coding sequence in upper case and lower case respectively
myDNA2 = 'ATCCTCGGTCGATTCAACTGTAAGTCCCATGAGTCGCTATCGTATTGGATCGATCTTGGATCGAATCGATCGCGATCGATCAAAATCATGCTATCTTTATCGATCGATATCGATGCATCGACTACTAT'
coding_exon1 = myDNA2[0:53].upper()
noncoding_intron = myDNA2[53:89].lower()
coding_exon2 = myDNA2[89:].upper()
new_myDNA2 = coding_exon1 + noncoding_intron + coding_exon2
print"The required sequence = " , new_myDNA2

