#!/usr/bin/python3
import csv
import requests
import sys


class Task:
    def __init__(self):
        self.file_inf = sys.argv[1]
        self.file_ouf = 'wikipedia_answers.csv'
        self.head_ouf = ["wikipedia_page", "website"]
        self.s_split = '</'
        self.s_compare = ['rel="nofollow" class="external', 'th>\n<td']
        self.s_start = 'href="'
        self.s_end = '"'

    def content(self, link):
        for line in requests.get(link[0]).text.split(self.s_split):
            if self.s_compare[0] in line and self.s_compare[1] in line:
                line = line[line.find(self.s_start) + len(self.s_start):]
                return line[:line.find(self.s_end)]

    def file_reading(self):
        with open(self.file_inf, 'r') as inf, open(self.file_ouf, 'w') as ouf:
            reader = csv.reader(inf, delimiter='\t')
            writer = csv.writer(ouf, quoting=csv.QUOTE_ALL)
            writer.writerow(self.head_ouf)
            for row in reader:
                writer.writerow([row[0], self.content(row)])

Task().file_reading()
