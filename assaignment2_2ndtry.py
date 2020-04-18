#!/bin/python3

import urllib.parse
import urllib.request
import re

import argparse
parser = argparse.ArgumentParser("DOWNLOAD STUFF")

parser.add_argument("userchoice",help="python 2.7.4, 3.3.1, or 3.2.4", choices=["a","b","c"])
print("choose wisley my master")
args=parser.parse_args()
if args.userchoice=="a":
    print("did you say a")
    print("yea im downloading yo")
    urllib.request.urlretrieve("https://www.python.org/downloads/release/python-274/", "Keelan_python_2.7.4")
    print("hey there im done downloading yo")

elif args.userchoice=="b":
    print("did you say b")
    print("yea im downloading yo")
    urllib.request.urlretrieve("https://www.python.org/downloads/release/python-331/","Keelan_python_3.3.1")
    print("hey there im done downloading yo")

elif args.userchoice=="c":
    print("did you say c")
    print("yea im downloading yo")
    urllib.request.urlretrieve("https://www.python.org/downloads/release/python-324", "Keelan_python_3.2.4")
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
