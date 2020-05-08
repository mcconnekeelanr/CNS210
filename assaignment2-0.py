#!/bin/python3

import urllib.parse
import urllib
import urllib.request
import re
import requests
from bs4 import BeautifulSoup
import argparse
parser = argparse.ArgumentParser("DOWNLOAD STUFF")

parser.add_argument("userchoice",help="python 2.7.4, 3.3.1, or 3.2.4", choices=["2.7.4", "3.3.1","3.2.4"])
print("choose wisley my master")
args=parser.parse_args()
if args.userchoice != None:
    print("did you say a")
    print("yea im downloading yo")
   # urllib.request.urlretrieve("https://www.python.org/ftp/python/" + args.userchoice + "/Python-" + args.userchoice + ".tar.xz", "keelan-python-" + args.userchoice + ".tar.xz")
    print("hey there im done downloading yo")


result = requests.get('https://python.org/downloads')
soup = BeautifulSoup(result.content, 'html.parser')
all_versions = soup.select('.download-list-widget .list-row-container li')
for version in all_versions:
    for i in version.select(".release-date"):
        if "April" in i.get_text():
            print(i.get_text())

            if "April 6, 2013" in i.get_text():
                print(version.select('.release-number')[0].get_text())
                print(version.select('.release-number')[0].get_text().split(" ")[1])
