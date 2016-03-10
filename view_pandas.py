"""
This part of the code comprises the view portion of model-view-controller. 
It takes in a model, which is a pandas dataframe with information about resources for queer youth in MA.
It outputs an interactive map using Bokeh. 

@author: Louise Nielsen and Apurva Raman
         nielsenlouise@github.com, apurvaraman@github.com
"""

from bokeh.models.widgets import CheckboxButtonGroup
from bokeh.models import (GMapPlot,
                          GMapOptions,
                          DataRange1d,
                          Circle,
                          PanTool,
                          WheelZoomTool,
                          BoxSelectTool,
                          HoverTool,
                          Legend)
from bokeh.io import show, output_file
import model_pandas as mdl

# let's define glyphs
red_glyph = Circle(size=15, fill_color='red', fill_alpha=.8)


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


class View(object):
    """Puts information from Model() on top of the nice gmap it got from Make_plot().
    """

    def __init__(self, filename='test.csv', model=None, plot=None, button=None):
        self.filename = filename
        if model is None:
            self.model = mdl.Model(self.filename)
        else:
            self.model = model
        if plot is None:
            x = Make_plot()
            self.plot = x.plot
        else:
            self.plot = plot
        if button is None:
            button = CheckboxButtonGroup(labels=['were trying', 'did we succeed'])
            self.button = button
        else:
            self.button = button

    def marker(self):
      """Defines a marker (a circle glyph) to represent a resource on the map.
      """
        self.model.set_color_stuff()
        circle = Circle(x='lon', y='lat', size=15, fill_color='color', fill_alpha=.8)
        self.plot.add_glyph(self.model.source, circle)

    def legend(self):
        red_glyph = self.plot.add_glyph(self.model.source, Circle(x='lon', y='lat', size=15, fill_color='red', fill_alpha=.8))
        Legend.legends = [
            ('health', red_glyph)]
#            ('support', green_glyph),
#            ('housing', blue_glyph),
#            ('advocacy', purple_glyph),
#            ('legal', cyan_glyph)]
        legend = Legend(location='bottom_left')
        self.plot.add_layout(legend)

    def hover_tool(self):
        """Makes the hover tool! Woot!
        """
        hover = self.plot.select_one(HoverTool)
        hover.point_policy = 'follow_mouse'
        hover.tooltips = [('Name', '@name'),
                          ('Address', '@address')]

    def buttons(self):
        """Makes buttons appear.

        Right now we're struggling with this because we probably have to use
        either a server or callbacks, one of which is being difficult and also
        one that involves a JS snippet.
        """
        pass

    def show_plot(self):
      """Outputs and displays a plot on a static webpage.
      """
        self.marker()
        self.hover_tool()
        self.legend()
        self.buttons()
        output_file('resources_plot.html')
        show(self.plot)


if __name__ == '__main__':
    thing = View()
    thing.show_plot()
