# Path Routing with Google Maps and OSMnx

This program calculates and plots the shortest path between two addresses in a city using the Google Maps API and the OSMnx library.

## Features

- **Address Geocoding:** Converts addresses into geographic coordinates (latitude and longitude) using the Google Maps API.
- **Street Network Graph Construction:** Creates a street network graph for the specified city using the OSMnx library.
- **Nearest Node Identification:** Finds the nearest nodes to the origin and destination coordinates on the graph.
- **Shortest Path Calculation:** Uses the A* algorithm to find the shortest path between the origin and destination nodes.
- **Path Plotting:** Plots the street graph with the shortest path highlighted, and marks the origin and destination points.

## Requirements

- Python 3.7+
- [Google Maps API Key](https://developers.google.com/maps/documentation/geocoding/get-api-key)
- Python Libraries:
  - `googlemaps`
  - `osmnx`
  - `networkx`
  - `matplotlib`

You can install the dependencies using the following command:

```bash
pip install googlemaps osmnx networkx matplotlib
```

## How to Use

# 1. Obtain a Google Maps API Key:
- Sign up at the Google Cloud Console.
- reate a project and enable the Geocoding API.
- Generate an API key and replace API_KEY in the code with your key.

# 2. Set the Origin and Destination Addresses:
- In the main script, enter the desired addresses for `address_A` and `address_B`.

# 3. Run the Script:
- The script will initialize the Google Maps client, convert the addresses to coordinates, build the street network graph, calculate the shortest path, and plot it on a graph.
- The coordinates and nearest nodes will be printed in the terminal.
# 4. Visualize the Result:
- The graph will display the shortest path between the two specified addresses, with the origin point in red and the destination point in yellow.






