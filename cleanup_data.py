import csv

import geopandas
import matplotlib.pyplot as plt
import pandas as pd

with open('downloads/Bigfoot_Locations.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    with open('bigfoot.csv', 'w') as output:
        spamwriter = csv.writer(output)
        for row in spamreader:
            new_row = []
            for item in row:
                item = item.replace('\n', ' ')
                item = item.strip('"')
                new_row.append(item)
            spamwriter.writerow(new_row)


df = pd.read_csv('bigfoot.csv')
df.index.name = 'id'

keep_columns = ['timestamp_', 'Lon', 'Lat', 'descriptio']
df = df[keep_columns]

renamed_columns = {'timestamp_': 'timestamp', 'Lat': 'latitude',
                   'Lon': 'longitude', 'descriptio': 'description'}
df = df.rename(columns=renamed_columns)

gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(
    df['longitude'], df['latitude'], crs="EPSG:4326"))

df.to_csv('bigfoot.csv')
gdf.to_file("bigfoot.geojson", driver='GeoJSON')
gdf.plot()
plt.show()
