```python
#!/usr/bin/env python
import re

gene_dict = {"gene_start":""}
output = ""
output_type = ["exon", "five_prime_UTR", "three_prime_UTR"]

with open("./stat_input.txt", "r") as f:
    while True:
        line = f.readline()

        if not line:
            break

        else:
            line_list = re.split("\t|\n", line)
            
            if line_list[1] == "gene":
                gene_dict["gene_start"] = line_list[2]
            elif line_list[1] in output_type:
                region_start = str(int(line_list[2]) - int(gene_dict["gene_start"])) 
                region_end = str(int(line_list[3]) - int(gene_dict["gene_start"]))
                output += line_list[0] + "\t" + line_list[1] + "\t" + region_start + "\t" + region_end + "\n"

file_output = open("gene_structure_temp.txt", "w")
file_output.write(output)
file_output.close()
```

