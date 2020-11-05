#!/usr/bin/env python3

gff="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz"
fasta="Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz"

import os,gzip,itertools,csv,re

def isheader(line):
    return line[0] == '>'

def aspairs(f):
    seq_id = ''
    sequence = ''
    for header,group in itertools.groupby(f, isheader):
        if header:
            line = next(group)
            seq_id = line[1:].split()[0]
        else:
            sequence = ''.join(line.strip() for line in group)
            yield seq_id, sequence

if not os.path.exists(gff):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/gff3/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.37.gff3.gz")

if not os.path.exists(fasta):
    os.system("curl -O ftp://ftp.ensemblgenomes.org/pub/bacteria/release-45/fasta/bacteria_0_collection/escherichia_coli_str_k_12_substr_mg1655/dna/Escherichia_coli_str_k_12_substr_mg1655.ASM584v2.dna.chromosome.Chromosome.fa.gz")
    
with gzip.open(gff,"rt") as fh:
    gff = csv.reader(fh,delimiter="\t")
    gene_count = 0

    for row in gff:
        if row[0].startswith("#"):
            continue
        if "gene" == row[2]:
            gene_count += 1
    print("total number of genes is",gene_count)

    total_genelen = 0
    for row in gff:
        if row[0].startswith("#"):
            continue 
        if "gene"==row[2]: 
            genelen = int(row[5])-int(row[4])
            total_genlen += genlen
    print("total gene length is",total_genelen)
