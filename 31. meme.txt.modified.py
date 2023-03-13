```python
#!/usr/bin/env python

import re
import argparse

parser = argparse.ArgumentParser(description='meme file stat')
parser.add_argument('-i', '--input_file', type=str, required=True, metavar='<file name>',
                    help='Input txt file the meme outputs, i.e., meme.txt')
parser.add_argument('-o', '--output_file', type=str, required=True, metavar='<file name>', help='output stat file')
args = parser.parse_args()

content = []
motif_order = 1
pattern1 = "Motif ([A-Z]+) MEME-[0-9]+ sites sorted by position p-value"
pattern2 = "Aco[0-9]+\s+[0-9]+\s+[0-9]+\.[0-9]+e-[0-9]+\s+[A-Z]+\s+[A-Z]+\s+[A-Z]+"
Motif_info_dict = {}
Motif_sample_dict = {}
seq_motif_info_all = []

with open(args.input_file) as f:
    while True:
        content_list = f.readline()

        # 1.先判断文件是否为空,如果不为空则去除换行符和制表符
        if not content_list:
            break
        else:
            content_list = content_list.replace("\t", "").replace("\n", "")
            if re.search("\+s", content_list):
                continue

        # 2.再判断是否为指定序列识别行"Motif motif序列 MEME-数字 sites sorted by position p-value"
        if re.search(pattern1, content_list):
            # 2.2 识别motif并把motif序列与长度信息存储到特定字典中
            match = re.findall(pattern1, content_list)
            # 2.2.1 模体名字信息
            Motif_name = "Motif" + str(motif_order)
            motif_order = int(motif_order) + 1
            # 2.2.2 存储模体序列信息
            Motif_sample_dict["seq"] = match[0]
            # 2.2.3 存储模体长度消息
            Motif_sample_dict["length"] = len(match[0])
            # 2.2.4 存储到Motif信息字典中
            Motif_info_dict[Motif_name] = Motif_sample_dict

        # 3.判断该行有无所需蛋白质序列号及其位置等关键信息
        if re.search(pattern2, content_list):
            # 拆分行为列表
            protein_motif_info_list = re.split("\s+", content_list)
            # 提取列表序列号和起始位置等信息
            seq_name = protein_motif_info_list[0]
            seq_start = int(protein_motif_info_list[1])
            seq_end = int(Motif_sample_dict["length"]) + int(seq_start) - 1
            seq_motif = Motif_name
            seq_motif_seq = str(protein_motif_info_list[4])
            seq_motif_info = [seq_name, seq_motif, seq_start, seq_end, seq_motif_seq]
            # 存储到最终要生成的表格
            seq_motif_info_all.append(seq_motif_info)

# 输出统计文件，第一列为蛋白质id，第二列为所属motif，第三列为motif开始位置，第四列为结束位置，第五列为模体序列
for i in seq_motif_info_all:
    output = i[0] + "\t" + i[1] + "\t" + str(i[2]) + "\t" + str(i[3]) + "\t" + i[4] + "\n"
    with open(args.output_file, "a") as f:
        f.write(output)
```

