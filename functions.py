import googlemaps
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

def inicializar_cliente_google_maps():
    gmaps = googlemaps.Client(key='substir_chave_api_google_maps')
    return gmaps

def geocodificar_endereco(gmaps, endereco):
    geocode_result = gmaps.geocode(endereco)
    coordenadas = geocode_result[0]['geometry']['location']
    return coordenadas

def construir_grafo_de_ruas(city):
    G = ox.graph_from_place(city, network_type='drive')
    return G

def encontrar_nos_mais_proximos(graph, latitude, longitude):
    no_mais_proximo = ox.distance.nearest_nodes(graph, longitude, latitude)
    return no_mais_proximo

def encontrar_caminho_mais_curto(graph, origem, destino):
    caminho_mais_curto = nx.astar_path(graph, source=origem, target=destino, weight='length')
    return caminho_mais_curto

def plotar_grafo_com_rota(G, rota, coord_origem, coord_destino):
    fig, ax = ox.plot_graph_route(G, rota, route_color='b', show=False, close=False)

    # Desenhar os pontos de origem e destino
    plt.plot(coord_origem['lng'], coord_origem['lat'], 'ro')  # ponto A (origem) em vermelho
    plt.plot(coord_destino['lng'], coord_destino['lat'], 'yo')  # ponto B (destino) em amarelo

    plt.show()

