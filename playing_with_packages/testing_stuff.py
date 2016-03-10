from bokeh.io import output_file, show
from bokeh.models import GeoJSONDataSource
from bokeh.plotting import figure
from bokeh.sampledata.sample_geojson import geojson


geo_source = GeoJSONDataSource(geojson=geojson)

p = figure()
p.circle(x='x', y='y', alpha=0.9, source=geo_source)
output_file("geojson.html")
show(p)
