import googlemaps
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Initialize the Google Maps API client.
def initialize_google_maps_client():
    gmaps = googlemaps.Client(key='API_KEY')
    return gmaps

# This function receives an address and a Google Maps client,
# geocodes the address using the provided client, and returns
# the corresponding geographic coordinates.
def geocode_address(gmaps, address):
    geocode_result = gmaps.geocode(address)
    coordinates = geocode_result[0]['geometry']['location']
    return coordinates

# This function builds a street graph for the provided city using the OSMnx library.
def build_street_graph(city):
    G = ox.graph_from_place(city, network_type='drive')
    return G

# This function finds the nearest node to the provided coordinates in the graph.
def find_nearest_node(graph, latitude, longitude):
    nearest_node = ox.distance.nearest_nodes(graph, longitude, latitude)
    return nearest_node

# This function finds and returns the shortest path between
# the origin and destination nodes in the street graph using the A* algorithm.
def find_shortest_path(graph, origin, destination):
    shortest_path = nx.astar_path(graph, source=origin, target=destination, weight='length')
    return shortest_path

# This function plots the graph with the route, marking the origin and destination points.
def plot_graph_with_route(G, route, origin_coords, destination_coords):
    fig, ax = ox.plot_graph_route(G, route, route_color='b', show=False, close=False)

    # Draw the origin and destination points
    plt.plot(origin_coords['lng'], origin_coords['lat'], 'ro')  # point A (origin) in red
    plt.plot(destination_coords['lng'], destination_coords['lat'], 'yo')  # point B (destination) in yellow

    plt.show()
