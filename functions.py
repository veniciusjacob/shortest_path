import googlemaps
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

#incialização da API.
def inicializar_cliente_google_maps():
    gmaps = googlemaps.Client(key='AIzaSyDzqv4Djq5ytLc0AF69LDGUyEr__UK71Os',)
    return gmaps

# essa função recebe um endereço e um cliente do Google Maps,
# realiza a geocodificação desse endereço usando o cliente fornecido e retorna
# as coordenadas geográficas correspondentes.
def converter_endereco(gmaps, endereco):
    geocode_result = gmaps.geocode(endereco)
    coordenadas = geocode_result[0]['geometry']['location']
    return coordenadas

#esta função constrói um grafo de ruas para a cidade fornecida, utilizando a biblioteca OSMnx.
def construir_grafo_de_ruas(cidade):
    G = ox.graph_from_place(cidade, network_type='drive')
    return G

#essa função encontra o nós mais próximo das coordenadas informadas
def encontrar_nos_mais_proximos(grafo, latitude, longitude):
    no_mais_proximo = ox.distance.nearest_nodes(grafo, longitude, latitude)
    return no_mais_proximo

#esta função encontra e retorna o caminho mais curto entre
#os nós de origem e destino no grafo de ruas, utilizando o algoritmo A*.
def encontrar_caminho_mais_curto(grafo, origem, destino):
    caminho_mais_curto = nx.astar_path(grafo, source=origem, target=destino, weight='length')
    return caminho_mais_curto

def plotar_grafo_com_rota(G, rota, coord_origem, coord_destino):
    fig, ax = ox.plot_graph_route(G, rota, route_color='b', show=False, close=False)

    # Desenhar os pontos de origem e destino
    plt.plot(coord_origem['lng'], coord_origem['lat'], 'ro')  # ponto A (origem) em vermelho
    plt.plot(coord_destino['lng'], coord_destino['lat'], 'yo')  # ponto B (destino) em amarelo

    plt.show()

