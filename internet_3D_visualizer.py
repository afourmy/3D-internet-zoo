import os
import warnings
from inspect import stack
try:
    import simplekml
except ImportError:
    warnings.warn('simplekml not installed: export to google earth disabled')
try:
    import networkx as nx
except ImportError:
    warnings.warn('networkx missing: "pip install networkx"')
        
path_app = os.path.dirname(os.path.abspath(stack()[0][1]))
path_graphs = os.path.join(path_app, 'dataset')
    
# style of a point in Google Earth
point_style = simplekml.Style()
point_style.labelstyle.color = simplekml.Color.blue
point_style.labelstyle.scale = 2
point_style.iconstyle.icon.href = 'https://raw.githubusercontent.com/afourmy/pyNMS/master/Icons/default_router.gif'

line_style = simplekml.Style()
line_style.linestyle.color = simplekml.Color.red
line_style.linestyle.width = 2

# associates a node name to its geodetic coordinates
node_coords = {}

kml = simplekml.Kml()

for file in os.listdir(os.path.join(path_app, 'dataset')):
    try:
        graph = nx.read_gml(os.path.join(path_graphs, file))
    except nx.exception.NetworkXError:
        continue
    for name, properties in graph.node.items():
        try:
            point = kml.newpoint(name=name)
            coords = [(float(properties['Longitude']), float(properties['Latitude']))]
            point.coords = coords
            node_coords[name] = coords
            point.style = point_style
        except KeyError:
            continue
    for link in graph.edges():
        try:
            name = '{} - {}'.format(*link)
            line = kml.newlinestring(name=name)
            line.coords = [node_coords[link[0]][0], node_coords[link[1]][0]]
            line.style = line_style
        except KeyError:
            continue
        
kml.save(os.path.join(path_app, 'google_earth_export.kml'))