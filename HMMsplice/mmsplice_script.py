# Import
from mmsplice.vcf_dataloader import SplicingVCFDataloader
from mmsplice import MMSplice, predict_save, predict_all_table
from mmsplice.utils import max_varEff
import pandas as pd

# example files
gtf = '/home/claudio/Repos/NIS/HMMsplice/gencode.v38.annotation.gtf'
vcf = '/home/claudio/Repos/NIS/HMMsplice/vcf_file.vcf.gz'
fasta = '/home/claudio/Repos/NIS/HMMsplice/chrom19.fasta'
csv = '/home/claudio/Repos/NIS/HMMsplice/pred_python.csv'

dl = SplicingVCFDataloader(gtf, fasta, vcf)

# Specify model
model = MMSplice()

# Or predict and return as df
predictions = predict_all_table(model, dl, pathogenicity=True, splicing_efficiency=True)

# Summerize with maximum effect size
predictionsMax = max_varEff(predictions)

predictions.to_csv("predictions.csv", sep=",")
predictionsMax.to_csv("predictionsMax.csv", sep=",")