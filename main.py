from functions import *

# Origin and destination addresses, prefer full addresses with ZIP codes.
address_A = 'R. Deusdete Coelho, 309 - Paraviana, 69307-273'
address_B = 'Av. Cap. Ene Garcês, 2413 - Bloco V - Aeroporto'
city = "Boa Vista"

print(f"Origin address: {address_A}")
print(f"Destination address: {address_B}")

# Initialize the Google Maps API client
gmaps = initialize_google_maps_client()

# Geocoding the addresses to obtain coordinates
coord_A = geocode_address(gmaps, address_A)
coord_B = geocode_address(gmaps, address_B)

# Check coordinates of the addresses (Uncomment if needed)
print(f"Origin Coordinates: {coord_A}")
print(f"Destination Coordinates: {coord_B}")

# Build the street network graph of the city
G = build_street_graph(city)

# Find the nearest node to the origin and destination
origin = find_nearest_node(G, coord_A['lat'], coord_A['lng'])
destination = find_nearest_node(G, coord_B['lat'], coord_B['lng'])

# Check the nearest node to the origin and destination (Uncomment if needed)
print("Nearest node to origin:", origin)
print("Nearest node to destination:", destination)

# Check all nodes in the graph (Uncomment if needed)
# print("Nodes in the graph:", G.nodes())

# Calculate the shortest path using the A* algorithm
shortest_path = find_shortest_path(G, origin, destination)

# Check nodes of the shortest path found (Uncomment if needed)
print("Shortest path found:", shortest_path)

# Plot the graph with the shortest path highlighted
plot_graph_with_route(G, shortest_path, coord_A, coord_B)
