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
