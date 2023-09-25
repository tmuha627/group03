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
tech_url02 = "https://www.cnbc.com/2023/09/22/vitalik-buterin-cnbc-interview-ethereum-founder-on-us-crypto-crackdown.html"
tech_page02 = requests.get(tech_url02)
techSoup02 = bs(tech_page02.text, 'html.parser')

#Grab specifics
tech_author02 = techSoup02.find_all(class_ = "Author-authorName")
tech_publishPlace02 = techSoup02.find_all(class_ = "CNBCFooter-copyright")
tech_publishDate02 = techSoup02.find_all("time", datetime="2023-09-22T12:00:01+0000")
tech_body02 = techSoup02.find_all(class_ = "group")

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
tech_url03 = "https://www.cnbc.com/2023/09/19/biden-to-work-with-world-leaders-to-ensure-ais-use-for-opportunity.html"
tech_page03 = requests.get(tech_url03)
techSoup03 = bs(tech_page03.text, 'html.parser')

#Grab specifics
tech_author03 = techSoup03.find_all("a", href="https://www.cnbc.com/lauren-feiner/")
tech_publishPlace03 = techSoup03.find_all(class_ = "CNBCFooter-copyright")
tech_publishDate03 = techSoup03.find_all("time", itemprop="datePublished")
tech_body03 = techSoup03.find_all(class_ = "group")

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
tech_url04 = "https://www.cnet.com/tech/computing/intel-plans-a-quantum-computing-approach-to-leapfrog-rivals/"
tech_page04 = requests.get(tech_url04)
techSoup04 = bs(tech_page04.text, 'html.parser')

#Grab specifics
tech_author04 = techSoup04.find_all("span", class_ ="c-globalAuthor_name")
tech_publishPlace04 = techSoup04.find_all(class_ = "c-siteFooter_copyright")
tech_publishDate04 = techSoup04.find_all("time")
tech_body04 = techSoup04.find_all("p")

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
tech_url05 = "https://www.the-scientist.com/news/a-rare-genetic-mutation-protects-against-alzheimer-s-disease-71374"
tech_page05 = requests.get(tech_url05)
techSoup05 = bs(tech_page05.text, 'html.parser')

#Grab specifics
tech_author05 = techSoup05.find_all("span", class_="author-name with-link")
tech_publishPlace05 = techSoup05.find_all("div", class_ ="copyRight")
tech_publishDate05 = techSoup05.find_all("time")
tech_body05 = techSoup05.find_all(class_ ="ArticleBody font-secondary fr-view")

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

#FOR ARTICLE 6
tech_url06 = "https://www.theverge.com/23885600/ios-ipados-interactive-widgets-dalle-3-amazon-echo-installer-newsletter"
tech_page06 = requests.get(tech_url06)
techSoup06 = bs(tech_page06.text, 'html.parser')

#Grab specifics
tech_author06 = techSoup06.find_all("a", href="/authors/david-pierce")
tech_publishPlace06 = techSoup06.find_all("title")
tech_publishDate06 = techSoup06.find_all("time", datetime="2023-09-24T12:00:00.000Z")
tech_body06 = techSoup06.find_all(class_ = "duet--article--article-body-component")

#paste into text document
techText06 = open("0306_tech.txt", mode="wt")

for authors in tech_author06:
    techText06.write("Author: " + authors.text)
    techText06.write('\n')

for places in tech_publishPlace06:
    techText06.write("Place of Publish: " + places.text)
    techText06.write('\n')

for date in tech_publishDate06:
    techText06.write("Published on: " + date.text)
    techText06.write('\n')

techText06.write("Body: " + '\n')
for body in tech_body06:
    techText06.write(body.text)
    techText06.write('\n')

techText06.close()

#FOR ARTICLE 7
tech_url07 = "https://www.theverge.com/2023/9/24/23887773/meta-ai-chatbots-gen-ai-personas-young"
tech_page07 = requests.get(tech_url07)
techSoup07 = bs(tech_page07.text, 'html.parser')

#Grab specifics
tech_author07 = techSoup07.find_all("a", href="/authors/wes-davis")
tech_publishPlace07 = techSoup07.find_all("title")
tech_publishDate07 = techSoup07.find_all("time", datetime="2023-09-24T19:30:44.098Z")
tech_body07 = techSoup07.find_all(class_ = "duet--article--article-body-component")

#paste into text document
techText07 = open("0307_tech.txt", mode="wt")

for authors in tech_author07:
    techText07.write("Author: " + authors.text)
    techText07.write('\n')

for places in tech_publishPlace07:
    techText07.write("Place of Publish: " + places.text)
    techText07.write('\n')

for date in tech_publishDate07:
    techText07.write("Published on: " + date.text)
    techText07.write('\n')

techText07.write("Body: " + '\n')
for body in tech_body07:
    techText07.write(body.text)
    techText07.write('\n')

techText07.close()

#FOR ARTICLE 8
tech_url08 = "https://www.theverge.com/2023/9/21/23883609/google-rcs-message-apple-iphone-ipager-ad"
tech_page08 = requests.get(tech_url08)
techSoup08 = bs(tech_page08.text, 'html.parser')

#Grab specifics
tech_author08 = techSoup08.find_all("a", href="/authors/jess-weatherbed")
tech_publishPlace08 = techSoup08.find_all("title")
tech_publishDate08 = techSoup08.find_all("time", datetime="2023-09-21T16:15:00.000Z")
tech_body08 = techSoup08.find_all(class_ = "duet--article--article-body-component")

#paste into text document
techText08 = open("0308_tech.txt", mode="wt")

for authors in tech_author08:
    techText08.write("Author: " + authors.text)
    techText08.write('\n')

for places in tech_publishPlace08:
    techText08.write("Place of Publish: " + places.text)
    techText08.write('\n')

for date in tech_publishDate08:
    techText08.write("Published on: " + date.text)
    techText08.write('\n')

techText08.write("Body: " + '\n')
for body in tech_body08:
    techText08.write(body.text)
    techText08.write('\n')

techText08.close()

#FOR ARTICLE 9
tech_url09 = "https://www.theverge.com/2023/9/21/23884863/valve-steam-deck-2-refresh-upgrade-cpu-2025"
tech_page09 = requests.get(tech_url09)
techSoup09 = bs(tech_page09.text, 'html.parser')

#Grab specifics
tech_author09 = techSoup09.find_all("a", href="/authors/sean-hollister")
tech_publishPlace09 = techSoup09.find_all("title")
tech_publishDate09 = techSoup09.find_all("time", datetime="2023-09-22T01:23:34.740Z")
tech_body09 = techSoup09.find_all(class_ = "duet--article--article-body-component")

#paste into text document
techText09 = open("0309_tech.txt", mode="wt")

for authors in tech_author09:
    techText09.write("Author: " + authors.text)
    techText09.write('\n')

for places in tech_publishPlace09:
    techText09.write("Place of Publish: " + places.text)
    techText09.write('\n')

for date in tech_publishDate09:
    techText09.write("Published on: " + date.text)
    techText09.write('\n')

techText09.write("Body: " + '\n')
for body in tech_body09:
    techText09.write(body.text)
    techText09.write('\n')

techText09.close()

#FOR ARTICLE 10
tech_url10 = "https://www.theverge.com/2023/9/24/23887975/nasa-asteroid-sample-osiris-rex-bennu-explained"
tech_page10 = requests.get(tech_url10)
techSoup10 = bs(tech_page10.text, 'html.parser')

#Grab specifics
tech_author10 = techSoup10.find_all("a", href="/authors/georgina-torbet")
tech_publishPlace10 = techSoup10.find_all("title")
tech_publishDate10 = techSoup10.find_all("time", datetime="2023-09-24T18:26:54.490Z")
tech_body10 = techSoup10.find_all(class_ = "duet--article--article-body-component")

#paste into text document
techText10 = open("0310_science.txt", mode="wt")

for authors in tech_author10:
    techText10.write("Author: " + authors.text)
    techText10.write('\n')

for places in tech_publishPlace10:
    techText10.write("Place of Publish: " + places.text)
    techText10.write('\n')

for date in tech_publishDate10:
    techText10.write("Published on: " + date.text)
    techText10.write('\n')

techText10.write("Body: " + '\n')
for body in tech_body10:
    techText10.write(body.text)
    techText10.write('\n')

techText10.close()