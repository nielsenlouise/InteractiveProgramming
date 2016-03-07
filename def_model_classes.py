"""We're gonna define some classes here, probably just one actually,
we'll figure it out."""


class Resources(object):
    """Resources() object contains a list of resources.
    """

    categories = ['health', 'LGB', 'T', 'etc']

    def __init__(self, list_resources):
        """initializes list_resources as an empty list.
        """
        pass

    def make_resource(self, filename, row):
        """Takes in filename and row for a csv file.

        Returns a list that is one resource created from that row.
        """
        pass

    def list_resources(self, filename):
        """Takes in filename.
        Calls make_resource.
        Modifies self.list_resources by populating it from csv file.
        """
        pass
