#!/usr/bin/python3
import csv
import requests
import sys

with open(sys.argv[1]) as inf, open('wikipedia_answers.csv', 'w') as ouf:
    reader = csv.reader(inf, delimiter="\t")
    writer = csv.writer(ouf, quoting=csv.QUOTE_ALL)
    writer.writerow(["wikipedia_page", "website"])
    for row in reader:
        for line in requests.get(row[0]).text.split('</'):
            if 'a rel="nofollow" class="external' in line and 'th>\n<td' in line:
                line = line[line.find('href="')+len('href="'):]
                writer.writerow([row[0], line[:line.find('"')]])
                break
