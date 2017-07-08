'''
Craft Data Engineer Intern Test Task
Developed by Bogorod V.O.
08-07-2017
'''
#!/usr/bin/python3
import csv
import requests
import sys


class Task:
    def __init__(self):
        self.file_inf = sys.argv[1]
        self.file_ouf = 'wikipedia_answers.csv'
        self.head_ouf = ["wikipedia_page", "website"]
        self.search = ['>Website<', 'href="', '"']

    def content(self, link):
        line = requests.get(link[0]).text
        line = line[line.find(self.search[0]):]
        line = line[line.find(self.search[1]) + len(self.search[1]):]
        return line[:line.find(self.search[2])]

    def file_reading(self):
        with open(self.file_inf, 'r') as inf, open(self.file_ouf, 'w') as ouf:
            reader = csv.reader(inf, delimiter='\t')
            writer = csv.writer(ouf, quoting=csv.QUOTE_ALL)
            writer.writerow(self.head_ouf)
            for row in reader:
                writer.writerow([row[0], self.content(row)])

Task().file_reading()
