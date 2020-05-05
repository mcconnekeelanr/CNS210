#!/bin/python3

import urllib.parse
import urllib
import urllib.request
import re

import argparse
parser = argparse.ArgumentParser("DOWNLOAD STUFF")

parser.add_argument("userchoice",help="python 2.7.4, 3.3.1, or 3.2.4", choices=["2.7.4", "3.3.1","3.3.2"])
print("choose wisley my master")
args=parser.parse_args()
if args.userchoice != None:
    print("did you say a")
    print("yea im downloading yo")
    urllib.request.urlretrieve("https://www.python.org/ftp/python/" + args.userchoice + "/Python-" + args.userchoice + ".tar.xz", "keelan-python-" + args.userchoice + ".tar.xz")
    print("hey there im done downloading yo")


print("now parsing python.org/downloads")
url = "http://www.python.org/downloads/"
values = {"s":"basics", "submit":"search"}

data = urllib.parse.urlencode(values)
data = data.encode ("utf-8")
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#print(respData)

#paragraphs is place holder, re.findall is the re module and findall command.
#in parenthisis <p> means paragraph tag so one means begining and other one is end
#stuff in between is some criteria were trying to find
paragraphs = re.findall(r"<p>(.*?)<p>",str(respData))
#. anything
#* 0 or more repetitions
#? 0 or 1 repetitions

#print(paragraphs)

for eachP in paragraphs:
    print(eachP)


#this took me a week to figure out lol looking at different examples and youtube videos
#now I want a pizza
