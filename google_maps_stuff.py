from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource as plotColumnDataSource
from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

map_options = GMapOptions(lat=42.3601, lng=-71.0589, map_type="roadmap", zoom=9)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="Austin"
)

# source = ColumnDataSource(
#    data=dict(
#        lat=[42.3601, 42.2926],
#        lon=[-71.0589, -71.2644],
#    )
# )

source = plotColumnDataSource(data=dict(
    x=[-71.0589, -71.2644],
    y=[42.3601, 42.2926],
    name=['Boston', 'Olin'],
    address=['Boston Rite Aid', 'Olin The Awesomest']
))

circle = Circle(x="x", y="y", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

TOOLS="pan,wheel_zoom,box_zoom,reset,hover,save"

p = figure(title="Our Map", tools=TOOLS)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), HoverTool())

hover = plot.select_one(HoverTool)
hover.point_policy = "follow_mouse"
hover.tooltips = [
    ('Name', '@name'),
    ('Title', '@address')
#    ("(Long, Lat)", "($x, $y)"),
]

# plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool(), hover())
output_file("gmap_plot.html")
show(plot)
