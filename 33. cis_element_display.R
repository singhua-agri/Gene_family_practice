```R
library(data.table)
library(tidyverse)
library(patchwork)

# 1.读入文件
cis <- fread("./DATA/plantCARE_output_PlantCARE_20618.txt",
             sep = "\t", header = F)

# 2.文件处理
cis_element <- c("ABRE", "AuxRR-core", "ERE", "CGTCA-motif", "GARE-motif", 
                 "TCA-element", "TGA-element", "ARE", "LTR", "MBS", "MYB",
                 "TC-rich", "W-box", "WUN-motif", "AE-box", "ACE", "ATCT-motif",
                 "I-box", "Box-4", "G-box", "GATA-motif")

new_cis <- filter(cis, V2 %in% cis_element) %>%
  select(name = V1, type = V2, length = V5) 
new_cis <- aggregate(length~type + name, new_cis, sum)
unique(new_cis$name)

# 画图
p1 <- ggplot() +
  geom_col(data = filter(new_cis, name %in% unique(new_cis$name)[1:17]),
           aes(x = name, fill = type, y = length),
           position = "stack",
           color = "black") +
  scale_y_continuous(expand = c(0, 0)) +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 45, 
                                   vjust = 0.5)) 

p2 <- ggplot() +
  geom_col(data = filter(new_cis, name %in% unique(new_cis$name)[18:36]),
           aes(x = name, fill = type, y = length),
           position = "stack",
           color = "black") +
  scale_y_continuous(expand = c(0, 0)) +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 45, 
                                   vjust = 0.5)) 

p3 <- ggplot() +
  geom_col(data = filter(new_cis, name %in% unique(new_cis$name)[37:54]),
           aes(x = name, fill = type, y = length),
           position = "stack",
           color = "black") +
  scale_y_continuous(expand = c(0, 0)) +
  theme_classic() +
  theme(axis.text.x = element_text(angle = 45, 
                                   vjust = 0.5)) 

p4 <- p1 / p2 / p3
p4 <- p4 + plot_layout(guides = 'collect')
p4

```

