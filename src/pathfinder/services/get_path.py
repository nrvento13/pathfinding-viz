import networkx as nx
from geopy.distance import geodesic   

# Define heuristic function for A*
def heuristic(node1, node2):
    return geodesic(node1, node2).meters

def get_path(G, start_node_coords, end_node_coords):
    """
    Get the shortest path between two nodes using the A* algorithm.

    Args:
        G (Graph): NetworkX graph containing the edges.
        start_node_coords (tuple): Coordinates of the start node (lat, lon).
        end_node_coords (tuple): Coordinates of the end node (lat, lon).

    Returns:
        path (list): List of nodes in the shortest path.
    """
    # Run A* algorithm
    path = nx.astar_path(
        G, 
        source=start_node_coords, 
        target=end_node_coords, 
        heuristic=heuristic, 
        weight='weight'
    )

    path = [(lon, lat) for lat, lon in path] 
    
    return path
