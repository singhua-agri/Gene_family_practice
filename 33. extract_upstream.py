```python
#!/usr/bin/env python

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import re

gene_family_dict = {}

# 1.gtf文件处理
with open("./aco.sbt.gtf", "r") as f:
    while True:
        file_line = f.readline()
        
        if not file_line:
            break

        else:
            file_line_list = re.split("\n|\t|\"", file_line)
            
            if file_line_list[2] == "transcript":
                gene_name = file_line_list[-3]
                chromosome = file_line_list[0]
                start = file_line_list[3]
                gene_family_dict[gene_name] = {"chr":chromosome, "start":start, "name":gene_name}

# 2.fasta文件读入
sequences_dict = SeqIO.index("../11.data/aco.fa", "fasta")

# 3.输出上游序列
for gene,info in gene_family_dict.items():
    start_point = int(info["start"]) - 2001
    end_point = int(info["start"]) - 1
    upstream = sequences_dict[info["chr"]].seq[start_point:end_point]
    upstream = SeqRecord(upstream, id=info["name"], description = "")

    with open("aco.sbt.fa", "a") as output_fa:
        SeqIO.write(upstream, output_fa, "fasta")
```

