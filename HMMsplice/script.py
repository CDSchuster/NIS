from Bio import SeqIO

genome=list(SeqIO.parse("GRCh38.p13.genome.fa", "fasta"))

records=[]
i=0
while genome[i].id != "chr19":
    i+=1

records.append(genome[i])

SeqIO.write(records, "chrom19.fasta", "fasta")
