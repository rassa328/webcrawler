from urllib.request import urlopen as uReq
import re
from urlextract import URLExtract
from urllib.request import Request, urlopen



visitedSites = []


headers = ({'User-Agent': 'Mozilla/5.0'})
my_url = 'http://lth.se'
request= Request(my_url, headers=headers)
HTMLNEW = urlopen(request).read().decode('utf-8')
extractor = URLExtract()
urls = extractor.find_urls(HTMLNEW)
visitedSites.append(my_url)
#print(visitedSites)
#print(urls)


print('--------------------------ovan är urls från lth.se-----------------')



def crawl():
    i=0
    for i in range(3):
            my_newurl = urls[i]
            visitedSites.append(my_newurl)
            request1= Request(my_newurl, headers=headers)
            HTMLNEW1= urlopen(request1).read().decode('latin-1')
            newExtractor = URLExtract()
            newurls = newExtractor.find_urls(HTMLNEW1)
            #print(newurls)
            #print('ovan är urls från:')
            #print(urls[i])
            #print('------------------NEW SITES!!!!!!!-------------')



crawl()
print(visitedSites)

def crawlAnotherLevel():
    k=0
    for k in range(3):
        myDeeperURLS=visitedSites[k+1]
        request2=Request(myDeeperURLS, headers=headers)
        HTMLNEW2=urlopen(request2).read().decode('latin-1')
        newerExtractor= URLExtract()
        newerurls = newerExtractor.find_urls(HTMLNEW2)
        j=0
        for j in range(3):
            visitedSites.append(newerurls[j])

        #print(newerurls)
        #print('------------------------')


crawlAnotherLevel()


def lastLevelCrawl():
    l=0
    for l in range(9):
        myDeepestURLS=visitedSites[l+4]
        request3=Request(myDeepestURLS, headers=headers)
        HTMLNEW3=urlopen(request3).read().decode('latin.1')
        newestExtractor = URLExtract()
        newesturls=newestExtractor.find_urls(HTMLNEW3)
        p=0
        for p in range(3):
            visitedSites.append(newesturls[p])

lastLevelCrawl()
print(visitedSites)
print(len(visitedSites))
