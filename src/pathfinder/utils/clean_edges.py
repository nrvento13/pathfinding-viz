def clean_edges(edges):
    """
    Cleans the edges GeoDataFrame by coverting any lists in the 'highway' column to strings.

    Args:
        edges (GeoDataFrame): A GeoDataFrame containing the edges of the road network.

    Returns:
        edges (GeoDataFrame): The cleaned GeoDataFrame.
    """
    edges['highway'] = edges['highway'].apply(lambda x: x[0] if isinstance(x, list) else x)
    return edges
