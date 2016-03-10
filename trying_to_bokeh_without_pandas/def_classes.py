"""We're gonna define some classes here, probably just one actually,
we'll figure it out."""


class Data(object):
    """Data() object contains a list of Resource() objects.
    """

    def __init__(self):
        """initializes as an empty list.
        """
        pass

    def make_resource(self, filename, row):
        """Takes in
        """
        pass

    def populate(self, filename):
        """
        """
        pass


class Resource(object):
    """Resource() object contains the information about a particular resource.

    Attributes: lat, lon, name, address, category"""

    def __init__(self,
                 lat, lon,
                 name='',
                 street='', city='', state='', zipcode='',
                 category=''):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.category = category

    def get_data(self, csv_file):
        """Takes in the name of a csv file.

        Returns
        """
        pass

    def location(self):
        """Takes in lat and lon.

        Returns a list where the zeroeth entry is the latitude and the first
        entry is longitude.
        """
        return [self.lat, self.lon]

    def address(self):
        """Takes in street, city, state, zip.

        Returns string of address.
        """
        return str(self.street) + str(self.city) + str(self.state) + str(self.zipcode)
