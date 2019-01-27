#!/usr/bin/env python 
#program to print the coding region of myDNA2
myDNA2 = 'ATCCTCGGTCGATTCAACTGTAAGTCCCATGAGTCGCTATCGTATTGGATCGATCTTGGATCGAATCGATCGCGATCGATCAAAATCATGCTATCTTTATCGATCGATATCGATGCATCGACTACTAT'
first_exon = myDNA2[0:53]
second_exon = myDNA2[89:]
coding_region = first_exon + second_exon 
print"coding region of myDNA2 = ",coding_region

