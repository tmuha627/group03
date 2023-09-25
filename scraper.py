import urllib
import requests
import re

from bs4 import BeautifulSoup as bs

#FOR ARTICLE 1
tech_url01 = "https://www.bbc.com/news/technology-66866577"
tech_page01 = requests.get(tech_url01)
techSoup01 = bs(tech_page01.text, 'html.parser')

#Grab specifics
tech_author01 = techSoup01.find_all(class_="ssrcss-68pt20-Text-TextContributorName e8mq1e96")
tech_publishPlace01 = techSoup01.find_all(class_ = "ssrcss-17ehax8-Cluster e1ihwmse1")
tech_publishDate01 = techSoup01.find_all("time", datetime="2023-09-21T11:56:58.000Z")
tech_body01 = techSoup01.find_all(class_ ="ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0")

#paste into text document
techText01 = open("0301_tech.txt", mode="wt")

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
tech_url02 = "https://www.cnn.com/2023/09/25/tech/amazon-invests-anthropic-ai/index.html"
tech_page02 = requests.get(tech_url02)
techSoup02 = bs(tech_page02.text, 'html.parser')

#Grab specifics
tech_author02 = techSoup02.find_all(class_ = "byline__names")
tech_publishPlace02 = techSoup02.find_all(class_ = "footer__copyright-text")
tech_publishDate02 = techSoup02.find_all(class_ = "timestamp")
tech_body02 = techSoup02.find_all(class_ = "article__content")
#paste into text document
techText02 = open("0302_tech.txt", mode="wt")

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
tech_url03 = "https://www.bbc.com/news/technology-66913551"
tech_page03 = requests.get(tech_url03)
techSoup03 = bs(tech_page03.text, 'html.parser')

#Grab specifics
tech_author03 = techSoup03.find_all(class_ = "ssrcss-68pt20-Text-TextContributorName e8mq1e96")
tech_publishPlace03 = techSoup03.find_all(class_ = "ssrcss-17ehax8-Cluster e1ihwmse1")
tech_publishDate03 = techSoup03.find_all("time", datetime="2023-09-25T16:02:36.000Z")
tech_body03 = techSoup03.find_all(class_ = "ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0")

#paste into text document
techText03 = open("0303_tech.txt", mode="wt")

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

#FOR ARTICLE 4
tech_url04 = "https://www.cnn.com/2023/09/25/tech/chatgpt-open-ai-humanlike-update/index.html"
tech_page04 = requests.get(tech_url04)
techSoup04 = bs(tech_page04.text, 'html.parser')

#Grab specifics
tech_author04 = techSoup04.find_all(class_ = "byline__name")
tech_publishPlace04 = techSoup04.find_all(class_ = "footer__copyright-text")
tech_publishDate04 = techSoup04.find_all(class_ = "timestamp")
tech_body04 = techSoup04.find_all(class_ = "article__content")
#paste into text document
techText04 = open("0304_tech.txt", mode="wt")

for authors in tech_author04:
    techText04.write("Author: " + authors.text)
    techText04.write('\n')

for places in tech_publishPlace04:
    techText04.write("Place of Publish: " + places.text)
    techText04.write('\n')

for date in tech_publishDate04:
    techText04.write("Published on: " + date.text)
    techText04.write('\n')

techText04.write("Body: " + '\n')
for body in tech_body04:
    techText04.write(body.text)
    techText04.write('\n')

techText04.close()

#FOR ARTICLE 5
tech_url05 = "https://www.bbc.com/news/science-environment-66893661"
tech_page05 = requests.get(tech_url05)
techSoup05 = bs(tech_page05.text, 'html.parser')

#Grab specifics
tech_author05 = techSoup05.find_all(class_="ssrcss-68pt20-Text-TextContributorName e8mq1e96")
tech_publishPlace05 = techSoup05.find_all(class_ ="ssrcss-17ehax8-Cluster e1ihwmse1")
tech_publishDate05 = techSoup05.find_all("time", datetime="2023-09-25T02:27:12.000Z")
tech_body05 = techSoup05.find_all(class_ = "ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0")

#paste into text document
techText05 = open("0305_science.txt", mode="wt")

for authors in tech_author05:
    techText05.write("Author: " + authors.text)
    techText05.write('\n')

for places in tech_publishPlace05:
    techText05.write("Place of Publish: " + places.text)
    techText05.write('\n')

for date in tech_publishDate05:
    techText05.write("Published on: " + date.text)
    techText05.write('\n')

techText05.write("Body: " + '\n')
for body in tech_body05:
    techText05.write(body.text)
    techText05.write('\n')

techText05.close()


