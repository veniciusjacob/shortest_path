from functions import *

#Endereços de origem e destino, priorizar endereços completos com CEP
endereco_A = 'R. Francisco Custodio de Andrade, 127'
endereco_B = 'Av. Cap. Ene Garcês, 2413 - Bloco V - Aeroporto'
cidade = "Boa vista"

# Inicialização do cliente da API do Google Maps
gmaps = inicializar_cliente_google_maps()

# Geocodificação dos endereços para obter as coordenadas
coord_A = converter_endereco(gmaps, endereco_A)
coord_B = converter_endereco(gmaps, endereco_B)

#Checar coordenas dos endereços(Descomentar)
# print(f"Coordenada Origem: {coord_A}")
# print(f"Coordenada Destino: {coord_B}")

# Construção do Grafo de Rede de Ruas da Cidade
G = construir_grafo_de_ruas(cidade)

#encontra o nó mais próximo da origem e o nó mais próximodo destino
origem = encontrar_nos_mais_proximos(G, coord_A['lat'], coord_A['lng'])
destino = encontrar_nos_mais_proximos(G, coord_B['lat'], coord_B['lng'])

#Checar nó de origem e nó de destino(descomentar)
# print("Nó de origem:", origem)
# print("Nó de destino:", destino)

#checar todos nós no grafo
#print("Nós no grafo:", G.nodes())

# Calculando o caminho mais curto usando o algoritmo A*
caminho_mais_curto = encontrar_caminho_mais_curto(G, origem, destino)

#Checar nós do caminho mais curto encontado(descomentar)
#print("Caminho mais curto encontrado:", caminho_mais_curto)

# Plotar o Grafo com o menor caminho destacado
plotar_grafo_com_rota(G, caminho_mais_curto, coord_A, coord_B)