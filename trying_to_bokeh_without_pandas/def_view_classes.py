"""here we're gonna define the classes we need for viewing the thing.
"""

from bokeh.models import HoverTool
from bokeh.plotting import figure
from bokeh.plotting import ColumnDataSource as plotColumnDataSource
from bokeh.io import output_file, show
from bokeh.models import (GMapPlot,
                          GMapOptions,
                          ColumnDataSource,
                          Circle,
                          DataRange1d,
                          PanTool,
                          WheelZoomTool,
                          BoxSelectTool)
import def_model_classes as mdl


class Make_plot(object):
    """Draws a plot. View does everything else, this is just there so that the
    plot does not have to be redrawn every time something is filtered.
    """

    def __init__(self, plot=None, map_type='roadmap', title='Resources'):
        self.map_type = map_type
        self.title = title
        if plot is None:
            map_options = GMapOptions(lat=42.3601, lng=-71.0589,
                                      map_type=self.map_type, zoom=9)
            plot = GMapPlot(x_range=DataRange1d(),
                            y_range=DataRange1d(),
                            map_options=map_options,
                            title=title)
            plot.add_tools(PanTool(),
                           WheelZoomTool(),
                           BoxSelectTool(),
                           HoverTool())
        self.plot = plot

    def return_plot(self):
        return self.plot


class View(object):
    """Takes in model and list of criteria.
    Returns interactive map.
    """

    def __init__(self, filename, model=None, plot=None, resources=None, criteria=['health', 'support']):
        if model is None:
            model = mdl.Model(filename)
        if plot is None:
            x = Make_plot()
            plot = Make_plot.return_plot(x)
        if resources is None:
            for item in model:
                resources = mdl.Model.make_dict(model[item], criteria)
        self.filename = filename
        self.model = model
        self.plot = plot
        self.resources = resources
        self.criteria = criteria

    def marker(self, categories):
        """Makes a circle of the color corresponding to its category.
        """
        colormap = {'health': 'blue', 'support': 'green'}
        colors = [colormap[x] for x in self.model['category']]
        self.list_resources(categories)
        circle = Circle(x="lon", y="lat", size=15, fill_color=colors, fill_alpha=0.8, line_color=None)
        self.plot.add_glyph(self.resources, circle)

    def list_resources(self, categories):
        """Calls Model.make_dict and plots it as ColumnDataSource.
        """
        self.resources = plotColumnDataSource(data=mdl.Model.make_dict(self.model, categories))

    def hover_tool(self):
        """Makes the hover tool! Woot!
        """
        hover = self.plot.select_one(HoverTool)
        hover.point_policy = 'follow_mouse'
        hover.tooltips = [('Name', '@name'),
                          ('Address', '@address')]

    def filter(self, catergories):
        """Takes in the categories that should be shown.

        Displays only the categories that should be shown.
        """
        pass

    def buttons_questionmarkquestionmarkquestionmark(self):
        """we're going to look into how to button.
        """
        pass

    def show_plot(self, categories):
        """Saves the plot as an html file and opens it in a browser tab.
        """
        self.list_resources(categories)
        self.marker(categories)
        self.hover_tool()
        output_file('resources_plot.html')
        show(self.plot)

if __name__ == '__main__':
    thing = View('test.csv')
    thing.show_plot(['health', 'support'])
