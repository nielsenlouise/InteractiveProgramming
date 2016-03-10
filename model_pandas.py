"""This file contains the model class using the pandas library (hooray!)
"""

from pandas import *
from bokeh.plotting import ColumnDataSource as plotColumnDataSource


class Model(object):
    """A Model() object contains a pandas.DataFrame of resources.
    """

    def __init__(self, source=None, filename='test.csv', frame=None):
        self.source = source
        self.filename = filename
        if frame is None:
            self.frame = DataFrame(read_csv(self.filename))
        else:
            self.frame = frame

    def set_color_stuff(self):
        colormap = {'health': 'red',
                    'support': 'green',
                    'housing': 'blue',
                    'advocacy': 'purple',
                    'legal': 'cyan'
                    }
        self.frame['color'] = self.frame['Category'].map(lambda x: colormap[x])
        self.source = plotColumnDataSource(dict(
                                      name=self.frame['Name'],
                                      lat=self.frame['Lat'],
                                      lon=self.frame['Lon'],
                                      address=self.frame['Address'],
                                      category=self.frame['Category'],
                                      color=self.frame['color']))

    def update_model(self):
        """This is going to update the model, probably has to filter things.
        """
        pass

if __name__ == '__main__':
    thing = Model()
    thing.set_color_stuff
    print thing.frame
