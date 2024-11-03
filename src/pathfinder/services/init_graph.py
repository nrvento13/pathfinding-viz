import networkx as nx  

def init_graph(edges):
    """
    Initialize a graph from a GeoDataFrame containing edges.

    Args:
        edges (GeoDataFrame): GeoDataFrame containing edges.

    Returns:
        G (Graph): NetworkX graph containing the edges.
    """

    # Initialize the graph
    G = nx.Graph()

    # Add edges to the graph
    for _, row in edges.iterrows():
        line = row['geometry']
        if line.geom_type == 'LineString':
            u = (line.coords[0][1], line.coords[0][0])  # Start node (lat, lon)
            v = (line.coords[-1][1], line.coords[-1][0])  # End node (lat, lon)
            length = row['length']
            
            # Add edge with distance as weight
            G.add_edge(u, v, weight=length)

    return G