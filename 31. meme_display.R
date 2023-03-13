```R
library(data.table)
library(tidyverse)

# 载入文本
pep_meme <- fread("./DATA/test.txt", header = F)
new_pep <- pep_meme %>%
  arrange(V1) %>%
  group_by(V1) 

pep_length <- fread("./DATA/length.stat.pep.txt", header = F)
pep_length <- mutate(pep_length, V3=0)

# 画图
ggplot() +
  geom_segment(data = new_pep, 
               aes(x = as.numeric(V3), 
                   y = V1,
                   xend = as.numeric(V4),
                   yend = V1,
                   color = V2),
               linewidth = 2.5, 
               position = position_nudge(y = 0.2)) +
  scale_color_brewer(palette = "Set3") +
  geom_segment(data = pep_length, 
               aes(x = as.numeric(V3),
                   y = V1,
                   xend = as.numeric(V2),
                   yend = V1),
               color = "grey",
               linewidth = 1) +
  scale_x_continuous(expand = c(0,0)) +
  labs(y = "Family",
       x = "Length",
       color = "Motif") +
  theme_classic()


```

