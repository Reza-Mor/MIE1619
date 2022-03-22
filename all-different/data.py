import csv
import os
import urllib.request
import zipfile


class all_different:
    dest_dir = '/Dataset/sudoku-hard/'

    def __init__(self):

        def read_csv(fname):
            print("Reading %s..." % fname)
            with open(self.dest_dir + fname) as f:
                reader = csv.reader(f, delimiter=',')
                return [(q, a) for q, a in reader]

        self.train = read_csv('train.csv')
        self.valid = read_csv('valid.csv')
        self.test = read_csv('test.csv')
