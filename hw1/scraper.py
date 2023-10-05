# By Group3 - Tyler Muha, Benjamin DeZutti, Bryan Zielcke, and Christian Goffredo
# Date: 9/25/2023 

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

#Article11
techURL11 = "https://www.cnbc.com/2023/09/21/cisco-acquiring-splunk-for-157-a-share-in-cash.html" 
techPage11 = requests.get(techURL11) 
techSoup11 = bs(techPage11.text, 'html.parser')

#Scrape Information
author11 = techSoup11.find_all(class_ = "Author-authorName")
publishPlace11 = techSoup11.find_all("title")
techDate11 = techSoup11.find_all("time", datetime = "2023-09-21T11:53:31+0000")
techBody11 = techSoup11.find(class_ = "group")

#Paste data into txt file   
techText11 = open("0311_tech.txt", mode = "wt")

for author in author11:
    techText11.write("Author: " + author.text)
    techText11.write("\n")

for loco in publishPlace11:
    techText11.write("Place of Publish: " + loco.text)
    techText11.write("\n") 

for date in techDate11:
    techText11.write("Date of Publish: "+ date.text)
    techText11.write("\n")

for body in techBody11:
    techText11.write("Body of Text: " + body.text)

techText11.close() 

#Article12
techURL12 = "https://www.cnbc.com/2023/09/18/google-dod-built-an-ai-powered-microscope-to-help-doctors-spot-cancer.html"
techPage12 = requests.get(techURL12)
techSoup12 = bs(techPage12.text, 'html.parser')

#Scrape Information
author12 = techSoup12.find_all(class_ ="Author-authorName")
publishPlace12 = techSoup12.find_all("title")
techDate12 = techSoup12.find_all("time", datetime = "2023-09-18T17:49:14+0000")
techBody12 = techSoup12.find(class_ = "group")


#Paste into txt file
techText12 = open("0312_tech.txt", mode = "wt")

for author in author12:
    techText12.write("Author: " + author.text)
    techText12.write("\n")

for place in publishPlace12:
    techText12.write("Place of Publish: " + place.text)
    techText12.write("\n")

for date in techDate12:
    techText12.write("Date of Publish: " + date.text)
    techText12.write("\n")

for body in techBody12:
    techText12.write("Body of Text: " + body.text)

techText12.close()

#Article13
techURL13 = "https://www.cnbc.com/2023/09/19/huaweis-chip-breakthrough-poses-new-threat-to-apple-in-china.html"
techPage13 = requests.get(techURL13)
techSoup13 = bs(techPage13.text, 'html.parser')

#Scrape Information
author13 = techSoup13.find_all(class_ = "Author-authorName")
publishPlace13 = techSoup13.find_all("title")
techDate13 = techSoup13.find_all("time", datetime = "2023-09-19T05:58:56+0000")
techBody13 = techSoup13.find(class_ = "group")

#Paste into txt file
techText13 = open("0313_tech.txt", mode = "wt")

for author in author13:
    techText13.write("Author: " + author.text)
    techText13.write("\n")

for place in publishPlace13:
    techText13.write("Place of Publish: " + place.text)
    techText13.write("\n")

for date in techDate13:
    techText13.write("Date of Publish: " + date.text)
    techText13.write("\n")

for body in techBody13:
    techText13.write("Body of Text: " + body.text)

techText13.close()

#Article14
techURL14 = "https://www.cnbc.com/2023/07/24/the-critical-cybersecurity-backup-plan-too-many-companies-are-ignoring.html" 
techPage14 = requests.get(techURL14)
techSoup14 = bs(techPage14.text, 'html.parser')

#Scrape Information
author14 = techSoup14.find_all(class_ = "Author-authorName")
publishPlace14 = techSoup14.find_all("title")
techDate14 = techSoup14.find_all("time", datetime = "2023-07-24T15:20:46+0000")
techBody14 = techSoup14.find(class_ = "group")

#Paste into txt file
techText14 = open("0314_tech.txt", mode = "wt")

for author in author14:
    techText14.write("Author: " + author.text)
    techText14.write("\n")

for place in publishPlace14:
    techText14.write("Place of Publish: " + place.text)
    techText14.write("\n")

for date in techDate14:
    techText14.write("Date of Publish: " + date.text)
    techText14.write("\n")

for body in techBody14:
    techText14.write("Body of Text: " + body.text)

techText14.close()

#Article15
scienceURL3 = "https://www.cnbc.com/2023/09/12/new-covid-vaccines-cdc-advisors-recommend-pfizer-and-moderna-shots.html"
sciencePage3 = requests.get(scienceURL3)
scienceSoup3 = bs(sciencePage3.text, 'html.parser')

#Scrape for information
author15 = scienceSoup3.find(class_ = "group")
publishPlace15 = scienceSoup3.find_all("title")
techDate15 = scienceSoup3.find_all("time", datetime = "2023-09-12T20:00:57+0000")
techBody15 = techSoup14.find(class_ = "group")

#Paste into txt file
techText15 = open("0315_science.txt", mode = "wt")

for author in author15:
    techText15.write("Author: " + author.text)
    techText15.write("\n")

for place in publishPlace15:
    techText15.write("Place of Publish: " + place.text)
    techText15.write("\n")

for date in techDate15:
    techText15.write("Date of Publish" + date.text)
    techText15.write("\n")

for body in techBody15:
    techText15.write("Body of Text: " + body.text)

techText15.close()

#FOR ARTICLE 16
tech_url16 = "https://www.bbc.com/news/technology-66866577"
tech_page16 = requests.get(tech_url16)
techSoup16 = bs(tech_page16.text, 'html.parser')

#Grab specifics
tech_author16 = techSoup16.find_all(class_="ssrcss-68pt20-Text-TextContributorName e8mq1e96")
tech_publishPlace16 = techSoup16.find_all(class_ = "ssrcss-17ehax8-Cluster e1ihwmse1")
tech_publishDate16 = techSoup16.find_all("time", datetime="2023-09-21T11:56:58.000Z")
tech_body16 = techSoup16.find_all(class_ ="ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0")

#paste into text document
techText16 = open("0316_tech.txt", mode="wt")

for authors in tech_author16:
    techText16.write("Author: " + authors.text)
    techText16.write('\n')

for places in tech_publishPlace16:
    techText16.write("Place of Publish: " + places.text)
    techText16.write('\n')

for date in tech_publishDate16:
    techText16.write("Published on: " + date.text)
    techText16.write('\n')

techText16.write("Body: " + '\n')
for body in tech_body16:
    techText16.write(body.text)
    techText16.write('\n')

techText16.close()

#FOR ARTICLE 17
tech_url17 = "https://www.cnn.com/2023/09/25/tech/amazon-invests-anthropic-ai/index.html"
tech_page17 = requests.get(tech_url17)
techSoup17 = bs(tech_page17.text, 'html.parser')

#Grab specifics
tech_author17 = techSoup17.find_all(class_ = "byline__names")
tech_publishPlace17 = techSoup17.find_all(class_ = "footer__copyright-text")
tech_publishDate17 = techSoup17.find_all(class_ = "timestamp")
tech_body17 = techSoup17.find_all(class_ = "article__content")
#paste into text document
techText17 = open("0317_tech.txt", mode="wt")

for authors in tech_author17:
    techText17.write("Author: " + authors.text)
    techText17.write('\n')

for places in tech_publishPlace17:
    techText17.write("Place of Publish: " + places.text)
    techText17.write('\n')

for date in tech_publishDate17:
    techText17.write("Published on: " + date.text)
    techText17.write('\n')

techText17.write("Body: " + '\n')
for body in tech_body17:
    techText17.write(body.text)
    techText17.write('\n')

techText17.close()

#FOR ARTICLE 18
tech_url18 = "https://www.bbc.com/news/technology-66913551"
tech_page18 = requests.get(tech_url18)
techSoup18 = bs(tech_page18.text, 'html.parser')

#Grab specifics
tech_author18 = techSoup18.find_all(class_ = "ssrcss-68pt20-Text-TextContributorName e8mq1e96")
tech_publishPlace18 = techSoup18.find_all(class_ = "ssrcss-17ehax8-Cluster e1ihwmse1")
tech_publishDate18 = techSoup18.find_all("time", datetime="2023-09-25T16:02:36.000Z")
tech_body18 = techSoup18.find_all(class_ = "ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0")

#paste into text document
techText18 = open("0318_tech.txt", mode="wt")

for authors in tech_author18:
    techText18.write("Author: " + authors.text)
    techText18.write('\n')

for places in tech_publishPlace18:
    techText18.write("Place of Publish: " + places.text)
    techText18.write('\n')

for date in tech_publishDate18:
    techText18.write("Published on: " + date.text)
    techText18.write('\n')

techText18.write("Body: " + '\n')
for body in tech_body18:
    techText18.write(body.text)
    techText18.write('\n')

techText18.close()

#FOR ARTICLE 19
tech_url19 = "https://www.cnn.com/2023/09/25/tech/chatgpt-open-ai-humanlike-update/index.html"
tech_page19 = requests.get(tech_url19)
techSoup19 = bs(tech_page19.text, 'html.parser')

#Grab specifics
tech_author19 = techSoup19.find_all(class_ = "byline__name")
tech_publishPlace19 = techSoup19.find_all(class_ = "footer__copyright-text")
tech_publishDate19 = techSoup19.find_all(class_ = "timestamp")
tech_body19 = techSoup19.find_all(class_ = "article__content")
#paste into text document
techText19 = open("0319_tech.txt", mode="wt")

for authors in tech_author19:
    techText19.write("Author: " + authors.text)
    techText19.write('\n')

for places in tech_publishPlace19:
    techText19.write("Place of Publish: " + places.text)
    techText19.write('\n')

for date in tech_publishDate19:
    techText19.write("Published on: " + date.text)
    techText19.write('\n')

techText19.write("Body: " + '\n')
for body in tech_body19:
    techText19.write(body.text)
    techText19.write('\n')

techText19.close()

#FOR ARTICLE 20
tech_url20 = "https://www.bbc.com/news/science-environment-66893661"
tech_page20 = requests.get(tech_url20)
techSoup20 = bs(tech_page20.text, 'html.parser')

#Grab specifics
tech_author20 = techSoup20.find_all(class_="ssrcss-68pt20-Text-TextContributorName e8mq1e96")
tech_publishPlace20 = techSoup20.find_all(class_ ="ssrcss-17ehax8-Cluster e1ihwmse1")
tech_publishDate20 = techSoup20.find_all("time", datetime="2023-09-25T02:27:12.000Z")
tech_body20 = techSoup20.find_all(class_ = "ssrcss-11r1m41-RichTextComponentWrapper ep2nwvo0")

#paste into text document
techText20 = open("0320_science.txt", mode="wt")

for authors in tech_author20:
    techText20.write("Author: " + authors.text)
    techText20.write('\n')

for places in tech_publishPlace20:
    techText20.write("Place of Publish: " + places.text)
    techText20.write('\n')

for date in tech_publishDate20:
    techText20.write("Published on: " + date.text)
    techText20.write('\n')

techText20.write("Body: " + '\n')
for body in tech_body20:
    techText20.write(body.text)
    techText20.write('\n')

techText20.close()