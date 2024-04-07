import googlemaps
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def initialize_google_maps_client():
    gmaps = googlemaps.Client(key='api_key')
    return gmaps

def geocode_address(gmaps, address):
    geocode_result = gmaps.geocode(address)
    coordinates = geocode_result[0]['geometry']['location']
    return coordinates

def build_street_network_graph(city):
    G = ox.graph_from_place(city, network_type='drive')
    return G

def find_nearest_nodes1(graph, latitude, longitude):
    nearest_node = ox.distance.nearest_nodes(graph, latitude, longitude)
    print("Nó mais próximo:", nearest_node)
    return nearest_node


def find_nearest_nodes(graph, latitude, longitude):
    nearest_node = ox.distance.nearest_nodes(graph, longitude, latitude)
    print("Nó mais próximo:", nearest_node)
    return nearest_node



def find_shortest_path(graph, source, target):
    shortest_path = nx.astar_path(graph, source=source, target=target, weight='length')
    return shortest_path



# Endereços de origem e destino
endereco_A = 'Rua Francisco Custódio de Andrade, 127'
endereco_B = 'Av. Cap. Ene Garcês, 2413 - Bloco V - Aeroporto'
cidade = "Boa vista"

# Inicialização do cliente da API do Google Maps
gmaps = initialize_google_maps_client()

# Geocodificação dos endereços para obter as coordenadas
coord_A = geocode_address(gmaps, endereco_A)
coord_B = geocode_address(gmaps, endereco_B)

#Checar coordenas dos endereços(Descomentar)
# print(f"Coordenada Origem: {coord_A}")
# print(f"Coordenada Destino: {coord_B}")

# Construção do Grafo de Rede de Ruas da Cidade
G = build_street_network_graph(cidade)

origem = find_nearest_nodes(G, coord_A['lat'], coord_A['lng'])
destino = find_nearest_nodes(G, coord_B['lat'], coord_B['lng'])

#Checar nó de origem e nó de destino(descomentar)
# print("Nó de origem:", origem)
# print("Nó de destino:", destino)

#checar todos nós no grafo(Descomentar)
#print("Nós no grafo:", G.nodes())

# Calculando o caminho mais curto usando o algoritmo A*
caminho_mais_curto = find_shortest_path(G, source=origem, target=destino)
print("Caminho mais curto encontrado:", caminho_mais_curto)

#Checar nós do caminho mais curto encontado(descomentar)
#print("Caminho mais curto encontrado:", caminho_mais_curto)

# Visualização do Grafo com o menor caminho destacado
fig, ax = ox.plot_graph_route(G, caminho_mais_curto, route_color='b', show=False, close=False)

# Desenhar os pontos de origem e destino
plt.plot(coord_A['lng'], coord_A['lat'], 'ro')  # ponto A (origem) em vermelho
plt.plot(coord_B['lng'], coord_B['lat'], 'yo')  # ponto B (destino) em amarelo

plt.show()
