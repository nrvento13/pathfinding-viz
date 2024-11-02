import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd

def plot_nodes_and_edges(
        nodes, 
        edges, 
        place_name, 
        start_node=None,
        end_node=None,
        figsize=(10, 10)
        ):
    fig, ax = plt.subplots(figsize=figsize)
    edges.plot(column="highway", legend=True, ax=ax, linewidth=1, alpha=0.7)
    nodes.plot(ax=ax, color='k', markersize=3, label="Nodes")
    # Convert start_node and end_node to GeoDataFrames if they're Series
    if start_node is not None:
        if isinstance(start_node, gpd.GeoSeries) or isinstance(start_node, pd.Series):
            start_node = gpd.GeoDataFrame(geometry=[start_node.geometry])
        start_node.plot(ax=ax, color='r', markersize=10, label="Start Node")
    
    if end_node is not None:
        if isinstance(end_node, gpd.GeoSeries) or isinstance(end_node, pd.Series):
            end_node = gpd.GeoDataFrame(geometry=[end_node.geometry])
        end_node.plot(ax=ax, color='g', markersize=10, label="End Node")
    
    plt.title("Road Network for {}".format(place_name))
    plt.legend()
    plt.show()