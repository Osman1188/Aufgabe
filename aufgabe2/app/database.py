import os
import os.path
import codecs
import csv
class Database_cl(object):
    def __init__(self):
        pass

    def readCsv(self):
        # Open the CSV file in read mode, using UTF-8 encoding.
        with codecs.open(os.path.join('data', 'students.csv'), 'r', 'utf-8') as csvfile:

            # Create a CSV reader object, using a comma as the delimiter.
            reader = csv.DictReader(csvfile, delimiter=',')

            # Read all the rows from the CSV file into a list of dictionaries.
            # Each dictionary represents a row, and the keys are the values in
            # the header row.
            return list(reader)
