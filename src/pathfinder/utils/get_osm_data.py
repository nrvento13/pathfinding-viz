import osmnx as ox
import geopandas as gpd
import pandas as pd

__all__ = [
    'get_area_boundary', 
    'get_osm_data_from_place', 
    'get_osm_data_from_poly', 
    'get_merged_polygon'
]

def get_area_boundary(place_name):
    """
    Retrieves the boundary of a place from OpenStreetMap.

    Args:
        place_name (str): The name of the place to retrieve the boundary for.

    Returns:
        area (GeoDataFrame): A GeoDataFrame containing the boundary of the place.
    """
    area = ox.geocode_to_gdf(place_name)
    return area

def get_osm_data_from_place(place, network_type='drive', custom_filter=None):
    """
    Connects to OpenStreetMap and retrieves the road network for a specified place.

    Args:
        place (str): The name of the place to retrieve the road network for.
        network_type (str): The type of network to retrieve (e.g., "drive", "walk", "bike"). Default is "drive".

    Returns:
        gdf_nodes (GeoDataFrame): A GeoDataFrame containing the nodes of the road network.
        gdf_edges (GeoDataFrame): A GeoDataFrame containing the edges of the road network.
    """
    # Get the road network for driving
    graph = ox.graph_from_place(
        place, 
        network_type=network_type, 
        custom_filter=custom_filter
    )

    # Convert the graph to a GeoDataFrame
    gdf_nodes, gdf_edges = ox.graph_to_gdfs(graph)

    return gdf_nodes, gdf_edges


def get_osm_data_from_poly(polygon, network_type='drive'):
    """
    Connects to OpenStreetMap and retrieves the road network for a specified bounding box.

    Args:
        area (pd.DataFrame): A DataFrame containing the boundary of the area to retrieve the road network for.
        network_type (str): The type of network to retrieve (e.g., "drive", "walk", "bike"). Default is "drive".

    Returns:
        gdf_nodes (GeoDataFrame): A GeoDataFrame containing the nodes of the road network.
        gdf_edges (GeoDataFrame): A GeoDataFrame containing the edges of the road network.
    """
    graph = ox.graph_from_polygon(polygon, network_type=network_type)
    gdf_nodes, gdf_edges = ox.graph_to_gdfs(graph)

    return gdf_nodes, gdf_edges

def get_merged_polygon(place_names):
    """
    Get the merged polygon of multiple places.

    Args:
        place_names (list): A list of place names to merge.

    Returns:
        polygon (GeoDataFrame): A GeoDataFrame containing the merged polygon.
    """

    areas = [get_area_boundary(place_name) for place_name in place_names]

    merged_area = gpd.GeoDataFrame(pd.concat(areas, ignore_index=True))
    polygon = merged_area['geometry'].unary_union

    return polygon