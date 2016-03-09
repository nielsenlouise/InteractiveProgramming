"""We're gonna define some classes here, probably just one actually,
we'll figure it out."""

import csv
import copy


class Model(object):
    """Model() object contains a list of resources.
    """

    def __init__(self, filename, list_resources=None):
        """initializes list_resources as an empty list.
        """
        if list_resources is None:
            list_resources = []
        self.list_resources = list_resources
        self.filename = filename

    def list_of_resources(self):
        """Takes in filename.
        Calls make_resource.
        Modifies self.list_resources by populating it from csv file.
        """
        resources = []
        with open(self.filename, 'rb') as csvfile:
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
            listlist = []
            for resource in self.list_resources:
                if resource[4] == category:
                    listlist.append(resource)
            filtered.append(listlist)
        return filtered
        # TODO: make this work for a resource having multiple categories

    def sort_by_cat(self, categories):
        """Takes in self. Calls list_of_resources.
        Returns a list of dictionaries where the contents of each dictionary
        only correspond to one category.
        """
        list_dicts = []
        for category in categories:
            print self.make_dict(category)
        #return list_dicts
        #should this just call filter resources?

    def make_dict(self, categories=None):
        """Takes in itself.
        Calls list_resources.
        Returns a dict of names, latitudes, longitudes, addresses, and
        categories.
        """
        self.list_of_resources()
        if categories is None:
            resources = self.list_resources
        else:
            resources = Model.filter_resources(self, categories)
        list_dicts = []
        print resources
        for type_resource in resources:
            names = []
            lats = []
            lons = []
            addresses = []
            categories = []
            for resource in type_resource:
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
            list_dicts.append(dict_resources)
        return list_dicts
