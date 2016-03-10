import pandas
from bokeh.plotting import ColumnDataSource as plotColumnDataSource
from bokeh.models import (GMapPlot,
                          GMapOptions,
                          DataRange1d,
                          Circle,
                          PanTool,
                          WheelZoomTool,
                          BoxSelectTool,
                          HoverTool)
from bokeh.io import show, output_file

test = pandas.read_csv('test.csv')
test2 = pandas.DataFrame(test)


types = ['health', 'support']

options = GMapOptions(lat=42.36, lng=-71.06, map_type='roadmap', zoom=11)
plot = GMapPlot(x_range=DataRange1d(),
                y_range=DataRange1d(),
                map_options=options,
                title='heh')
plot.add_tools(PanTool(),
               WheelZoomTool(),
               BoxSelectTool(),
               HoverTool())

colormap = {'health': 'red', 'support': 'green'}
test2['color'] = test2['Category'].map(lambda x: colormap[x])

source = plotColumnDataSource(dict(
                              name=test2['Name'],
                              lat=test2['Lat'],
                              lon=test2['Lon'],
                              address=test2['Address'],
                              category=test2['Category'],
                              color=test2['color']))
print source


class Model(object):
    """A Model() object contains a pandas.DataFrame of resources.
    """

    def __init__(self, filename='test.csv', frame=None):
        self.filename = filename
        self.frame = pandas.DataFrame(pandas.read_csv(self.filename))


class View(object):
    """I'm not really sure what this class is going to do. I guess I'll figure
    it out.
    """

    def __init__(self, types, filename='test.csv', model=None):
        self.types = types
        self.filename = filename
        if model is None:
            self.model = Model(self.filename)
        else:
            self.model = model

    def make_map(self, map_type, title):
        options = GMapOptions(lat=43.7, lng=-79.4, map_type=map_type, zoom=11)
        plot = GMapPlot(x_range=DataRange1d(),
                        y_range=DataRange1d(),
                        map_options=options,
                        title=title)
        output_file('plot.html')
        show(plot)


circle = Circle(x='lon', y='lat', size=15, fill_color='color', fill_alpha=.8)
plot.add_glyph(source, circle)

output_file('heh.html')
show(plot)
