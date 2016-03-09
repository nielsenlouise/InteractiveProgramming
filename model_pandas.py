"""This file contains the model class using the pandas library (hooray!)
"""

import pandas
from bokeh.plotting import ColumnDataSource as plotColumnDataSource


class Model(object):
    """A Model() object contains a pandas.DataFrame of resources.
    """

    def __init__(self, source, filename='test.csv', frame=None):
        self.source = source
        self.filename = filename
        if frame is None:
            self.frame = pandas.DataFrame(pandas.read_csv(self.filename))
        else:
            self.frame = frame

    def set_color_stuff(self):
        colormap = {'health': 'blue', 'support': 'green'}
        self.frame['color'] = self.frame['Category'].map(lambda x: colormap[x])
        self.source = plotColumnDataSource(dict(
                                      name=self.frame['Name'],
                                      lat=self.frame['Lat'],
                                      lon=self.frame['Lon'],
                                      address=self.frame['Address'],
                                      category=self.frame['Category'],
                                      color=self.frame['color']))
