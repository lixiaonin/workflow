import csv
from random import randint


class DatasetGenerator(object):

    def __init__(self, filename):
        self.filename = filename

    def _gen_line(self, cols):
        return '\t'.join(cols) + '\n'

    def _header(self):
        return self._gen_line([
            'Rank', 
            'Port', 
            'Volume 2015', 
            'Volume 2014', 
            'Volume 2013', 
            'Volume 2012', 
            'Volume 2011'
            ])

    def _data_row(self):
        rank = str(randint(0,500000))
        port_name = 'city_name_%d, country_name_%d' % (randint(100000,200000), randint(10000,20000))
        v2015 = str(randint(100,3600)/100.0)
        v2014 = str(randint(100,3600)/100.0)
        v2013 = str(randint(100,3600)/100.0)
        v2012 = str(randint(100,3600)/100.0)
        v2011 = str(randint(100,3600)/100.0)
        return self._gen_line([rank, port_name, v2015, v2014, v2013, v2012, v2011])

    def _gen_file(self):
        with open(self.filename, "w") as mytsv:
            mytsv.write(self._header())
            for i in xrange(10000):
                mytsv.write(self._data_row())


if __name__ == "__main__":
    mydg = DatasetGenerator('dataset002.tsv')
    mydg._gen_file()
