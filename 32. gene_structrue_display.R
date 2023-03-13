```R
library(data.table)
library(tidyverse)

# 载入文本
cds_length <- fread("./DATA/aco.sbt.gene.length.txt", header = F)
cds_length <- mutate(cds_length, V3=0)

gene_structure <- fread("./DATA/gene_structure_temp.txt", header = F)

# 画图
ggplot() +
  geom_segment(data = gene_structure, 
               aes(x = as.numeric(V3), 
                   y = V1,
                   xend = as.numeric(V4),
                   yend = V1,
                   color = V2),
               linewidth = 2.5, 
               position = position_nudge(y = 0.2)) +
  scale_color_brewer(palette = "Set2") +
  geom_segment(data = cds_length, 
               aes(x = as.numeric(V3),
                   y = V1,
                   xend = as.numeric(V2),
                   yend = V1),
               color = "grey",
               linewidth = 1) +
  scale_x_continuous(expand = c(0,0)) +
  labs(y = "Family",
       x = "Length",
       color = "Structure") +
  theme_classic()

```

