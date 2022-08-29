from cgi import print_directory
import colorgram



cores = colorgram.extract("imagem/48_001.jpg",10)
print(cores)
importado_cores = []
for cor in cores:
    importado_cores.append(cor.rgb)

print(importado_cores)