#!/usr/bin/env python3
f = open("data.csv")
for line in f:
     column = line.rstrip("\n").split(",")
     org_name = column[0]
     gene_seq = column[1]
     org_name = column[0]
     exp_level = column[3]
     if len(gene_seq) > 90 and len(gene_seq) < 110:
          print(gene_seq)
