from Bio import SeqIO

msa=list(SeqIO.parse("prots_msa_filt.fasta", "fasta"))

IDs=[rec.id.split("|")[1] for rec in msa]

outf=open("IDs", "w")

for ID in IDs: print(ID, file=outf)