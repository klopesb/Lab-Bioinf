from Bio.Blast import NCBIXML 
from Bio.Blast import NCBIWWW 
from Bio import SeqIO


#Ler os arquivos em formato fasta
#record_gh20 =  SeqIO.read(open("Add your fasta here.fasta"), format="fasta")    #Gene GH20

#record_gh42 =  SeqIO.read(open("Add your fasta here.fasta"), format="fasta")    #Gene GH42

record_gh95 = SeqIO.read(open(r"trabalho_LB\blast\GH95.fasta"), format="fasta")    #Gene GH95

#record_gh33 =  SeqIO.read(open("Add your fasta here.fasta"), format="fasta")    #Gene GH33

#Executar blast 

# result_handle_gh20 = NCBIWWW.qblast("blastp", "nr", record.format("fasta"))

# result_handle_gh42 = NCBIWWW.qblast("blastp", "nr", record.format("fasta"))

result_handle_gh95 = NCBIWWW.qblast("blastp", "nr", record_gh95.format("fasta"))

# result_handle_gh33 = NCBIWWW.qblast("blastp", "nr", record.format("fasta"))





