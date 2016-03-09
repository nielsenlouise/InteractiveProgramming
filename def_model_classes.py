"""We're gonna define some classes here, probably just one actually,
we'll figure it out."""

import csv


class Model(object):
    """Model() object contains a list of resources.
    """

    categories = ['health', 'LGB', 'T', 'etc']

    def __init__(self, list_resources=None):
        """initializes list_resources as an empty list.
        """
        if list_resources is None:
            list_resources = []
        self.list_resources = list_resources

    def list_resources(self, filename):
        """Takes in filename.
        Calls make_resource.
        Modifies self.list_resources by populating it from csv file.
        """
        resources = []
        with open(filename, 'rb') as csvfile:
            read_resource = csv.reader(csvfile)
            for row in read_resource:
                resources.append(row)
        del resources[0]
        self.list_resources = resources

    def filter_resources(self, categories):
        """Takes in a list of categories.

        Returns a new list that contains only resources of those categories.
        """
        filtered = []
        for category in categories:
            for resource in self.list_resources:
                if resource[4] == category:
                    filtered.append(resource)
        return filtered
        # TODO: make this work for a resource having multiple categories

    def make_dict(self, categories=None):
        """Takes in itself.
        Calls list_resources.
        Returns a dict of names, latitudes, longitudes, addresses, and
        categories.
        """
        if categories is None:
            resources = self.list_resources
        else:
            resources = self.filter_resources(categories)
        names = []
        lats = []
        lons = []
        addresses = []
        categories = []
        for resource in resources:
            names.append(resource[0])
            lats.append(resource[1])
            lons.append(resource[2])
            addresses.append(resource[3])
            categories.append(resource[4])
        dict_resources = {'name': names,
                          'lat': lats,
                          'lon': lons,
                          'address': addresses,
                          'category': categories}
        return dict_resources
