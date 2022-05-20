import geojson
from shapely import wkt
from shapely.geometry import shape
from pandas import read_excel, DataFrame, to_numeric, isnull

with open('myfile.geojson') as f:
    geojson_content = geojson.load(f)

geojson_features = geojson_content['features']

df = DataFrame()

for x in geojson_features:
    
    row = geojson_features.index(x)
    geometry_feature = x['geometry']
    geometry_shape = shape(geometry_feature)
    wkt_geometry = wkt.loads(geometry_shape.wkt)
    df.at[row, 'WKT'] = wkt_geometry
    properties_feature = x['properties']
    for i in properties_feature:
        if properties_feature[i] == None:
            df.at[row, i] = ''
        else: df.at[row, i] = properties_feature[i]
        
df.to_excel('geojson_convert_result.xlsx', index=False)        
df.to_csv('geojson_convert_result.csv', index=False)
