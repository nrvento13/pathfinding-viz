import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString

def plot_area(
        nodes=None, 
        edges=None, 
        start_node=None,
        end_node=None,
        path=None,
        figsize=(10, 10),
        title="Road Network"
        ):
    
    """
    Plots the road network with nodes, edges, start_node and end_node.

    Args:
        nodes (GeoDataFrame): GeoDataFrame of nodes.
        edges (GeoDataFrame): GeoDataFrame of edges.
        start_node (GeoDataFrame or GeoSeries): GeoDataFrame or GeoSeries of start node.
        end_node (GeoDataFrame or GeoSeries): GeoDataFrame or GeoSeries of end node.
        path (list): List of node coordinates representing the path.
        figsize (tuple): Size of the plot.
        title (str): Title of the plot.

    Returns:
        None
    """
    fig, ax = plt.subplots(figsize=figsize)
    if edges is not None:
        edges.plot(column="highway", legend=True, ax=ax, linewidth=1, alpha=0.5)
    
    if nodes is not None:
        nodes.plot(ax=ax, color='k', markersize=3, label="Nodes")
        
    # Convert start_node and end_node to GeoDataFrames if they're Series
    if start_node is not None:
        if isinstance(start_node, gpd.GeoSeries) or isinstance(start_node, pd.Series):
            start_node = gpd.GeoDataFrame(geometry=[start_node.geometry])
        start_node.plot(ax=ax, color='r', markersize=20, marker='*', label="Start Node")
    
    if end_node is not None:
        if isinstance(end_node, gpd.GeoSeries) or isinstance(end_node, pd.Series):
            end_node = gpd.GeoDataFrame(geometry=[end_node.geometry])
        end_node.plot(ax=ax, color='g', markersize=20, marker='*', label="End Node")
    
    # Plot the path as a line
    if path is not None:
        # Convert path to a LineString if it's a list of coordinates
        if isinstance(path, list) and all(isinstance(coord, tuple) for coord in path):
            path_line = gpd.GeoDataFrame(geometry=[LineString(path)])
            path_line.plot(ax=ax, color='blue', linewidth=2, label="Path")

    plt.title(title)
    plt.legend()
    plt.show()