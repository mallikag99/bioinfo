f = open("data.csv")
for line in f:
     columns = line.rstrip("\n").split(",")
     org_name = columns[0]
     gene_seq = columns[1]
     gene_name = columns[2]
     exp_level = columns[3]
     if (gene_name.startswith("A") or gene_name.startswith("D") and org_name != "Homo sapiens") and int(exp_level) > 160:
         print(gene_name)
