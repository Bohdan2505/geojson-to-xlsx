import json
from geojson import Polygon, Feature, FeatureCollection
from pandas import read_excel, DataFrame, to_numeric
import shapely.wkt
import numpy as np

file_location = 'geojson_convert_result.xlsx'
df = read_excel(file_location)
df.fillna('', inplace=True)
GEOJSON_FEATURES = []
CRS = {"type": "name", "properties": {"name": "EPSG:4326"}}

for row in range(df.shape[0]):
    properties_feature = {}
    #geometry_feature = {}
    geometry_feature = shapely.wkt.loads(df.at[row, 'WKT'])
    
    for x in df.columns[1:]:
        if isinstance(df.at[row, x], np.floating):
            properties_feature[x] = float(df.at[row, x])
        if isinstance(df.at[row, x], np.integer):
            properties_feature[x] = int(df.at[row, x])
        else: properties_feature[x] = df.at[row, x]
       
    GEOJSON_FEATURES.append(Feature(geometry=geometry_feature, properties=properties_feature))

GEOJSON_CONTENT = FeatureCollection(GEOJSON_FEATURES, crs=CRS)

with open('convert.geojson', 'w') as f:
    json.dump(GEOJSON_CONTENT, f, indent=2, sort_keys=True)
