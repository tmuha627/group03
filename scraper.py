import urllib
import requests
import re

from bs4 import BeautifulSoup as bs

#FOR ARTICLE 1
tech_url01 = "https://www.theverge.com/2023/9/21/23882988/intel-innovation-2023-announcements-meteor-lake-lunar-panther-xeon"
tech_page01 = requests.get(tech_url01)
techSoup01 = bs(tech_page01.text, 'html.parser')

#Grab specifics
tech_author01 = techSoup01.find_all("a", href="/authors/monica-chin")
tech_publishPlace01 = techSoup01.find_all("title")
tech_publishDate01 = techSoup01.find_all("time", datetime="2023-09-21T22:41:26.740Z")
tech_body01 = techSoup01.find_all(class_ = "duet--article--article-body-component")

#paste into text document
techText01 = open("group03/0301_tech.txt", mode="wt")

for authors in tech_author01:
    techText01.write("Author: " + authors.text)
    techText01.write('\n')

for places in tech_publishPlace01:
    techText01.write("Place of Publish: " + places.text)
    techText01.write('\n')

for date in tech_publishDate01:
    techText01.write("Published on: " + date.text)
    techText01.write('\n')

techText01.write("Body: " + '\n')
for body in tech_body01:
    techText01.write(body.text)
    techText01.write('\n')

techText01.close()

#FOR ARTICLE 2
tech_url02 = "https://www.cnbc.com/2023/09/22/vitalik-buterin-cnbc-interview-ethereum-founder-on-us-crypto-crackdown.html"
tech_page02 = requests.get(tech_url02)
techSoup02 = bs(tech_page02.text, 'html.parser')

#Grab specifics
tech_author02 = techSoup02.find_all(class_ = "Author-authorName")
tech_publishPlace02 = techSoup02.find_all(class_ = "CNBCFooter-copyright")
tech_publishDate02 = techSoup02.find_all("time", datetime="2023-09-22T12:00:01+0000")
tech_body02 = techSoup02.find_all(class_ = "group")

#paste into text document
techText02 = open("group03/0302_tech.txt", mode="wt")

for authors in tech_author02:
    techText02.write("Author: " + authors.text)
    techText02.write('\n')

for places in tech_publishPlace02:
    techText02.write("Place of Publish: " + places.text)
    techText02.write('\n')

for date in tech_publishDate02:
    techText02.write("Published on: " + date.text)
    techText02.write('\n')

techText02.write("Body: " + '\n')
for body in tech_body02:
    techText02.write(body.text)
    techText02.write('\n')

techText02.close()

#FOR ARTICLE 3
tech_url03 = "https://www.cnbc.com/2023/09/19/biden-to-work-with-world-leaders-to-ensure-ais-use-for-opportunity.html"
tech_page03 = requests.get(tech_url03)
techSoup03 = bs(tech_page03.text, 'html.parser')

#Grab specifics
tech_author03 = techSoup03.find_all("a", href="https://www.cnbc.com/lauren-feiner/")
tech_publishPlace03 = techSoup03.find_all(class_ = "CNBCFooter-copyright")
tech_publishDate03 = techSoup03.find_all("time", itemprop="datePublished")
tech_body03 = techSoup03.find_all(class_ = "group")

#paste into text document
techText03 = open("group03/0303_tech.txt", mode="wt")

for authors in tech_author03:
    techText03.write("Author: " + authors.text)
    techText03.write('\n')

for places in tech_publishPlace03:
    techText03.write("Place of Publish: " + places.text)
    techText03.write('\n')

for date in tech_publishDate03:
    techText03.write("Published on: " + date.text)
    techText03.write('\n')

techText03.write("Body: " + '\n')
for body in tech_body03:
    techText03.write(body.text)
    techText03.write('\n')

techText03.close()
