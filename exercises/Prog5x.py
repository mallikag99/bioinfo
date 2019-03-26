#!/usr/bin/env python3
open("data.csv")
for line in f:
     columns = line.rstrip("\n").split(",")
     org_name = columns[0]
     gene_seq = columns[1]
     gene_name = columns[2]
     exp_level = columns[3]
     lp = len(gene_seq)
     g_count = gene_seq.count("g")
     c_count = gene_seq.count("c")
     gc_content = (g_count + c_count)/lp
     if gc_content > 0.65:
         print(gene_name + " has high GC content")
     elif gc_content < 0.45:
         print(gene_name + " has low GC content")
     else:
         print(gene_name + " has medium GC content")
