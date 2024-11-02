from scipy.spatial import distance

def find_nearest_node(nodes, point):
    coordinates = nodes[['y', 'x']].values
    nearest = distance.cdist([point], coordinates).argmin()
    return nodes.iloc[nearest]