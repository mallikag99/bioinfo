#!/usr/bin/env python3
f = open("data.csv")
for line in f:
     column = line.rstrip("\n").split(",")
     if column[0] == "Homo sapiens" or column[0] == "Pan troglodytes":
         print(column[0:6])
