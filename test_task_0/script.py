#!/usr/bin/python3
import csv
import requests
import sys

with open(sys.argv[1]) as inf, open('wikipedia_answers.csv', 'w') as ouf:
    reader = csv.reader(inf, delimiter="\t")
    writer = csv.writer(ouf, quoting=csv.QUOTE_ALL)
    writer.writerow(["wikipedia_page","website"])
    for row in reader:
        for line in requests.get(row[0]).text.split('</'):
            if 'rel="nofollow" class="external' in line:
                if 'th>\n<td' in line:
                    if 'http' in line:
                        line = line[line.find('http'):]
                    else:
                        line = line[line.find('www'):]
                    writer.writerow([row[0],line[:line.find('"')]])
                    break
