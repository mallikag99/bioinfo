#!/usr/bin/env python3
f = open("data.csv")
for line in f:
     column = line.rstrip("\n").split(",")
     org_name = column[0]
     gene_seq = column[1]
     g_count = gene_seq.count("g")
     c_count = gene_seq.count("c")
     lp = len(gene_seq)
     gc_content = (g_count + c_count)/lp
     if gc_content < 0.5:
         print(org_name)
