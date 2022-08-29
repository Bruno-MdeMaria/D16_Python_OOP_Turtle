import random
import colorgram



cores = colorgram.extract("imagem/48_001.jpg",50)
print(cores)
importado_cores = []
for cor in cores:
    r = cor.rgb.r
    g = cor.rgb.g
    b = cor.rgb.b
    nova_cor = (r, g , b)
    importado_cores.append(nova_cor)

print(importado_cores)