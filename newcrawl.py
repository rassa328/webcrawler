from urllib.request import urlopen as uReq
import re
from urlextract import URLExtract
from urllib.request import Request, urlopen
from urllib.parse import urlparse
import ssl

####################################################################
ssl._create_default_https_context = ssl._create_unverified_context
visitedUrls = []

#Strips the url to only domain and add http://www. if needed
def convert(url):
    try:
        url = urlparse(url).hostname
        if url.startswith('www.'):
            return 'http://' + url
        if not url.startswith('www'):
            return 'http://www.' + url
        return url
    except:
        pass

#Remove all duplicates in list
def dupRemove(list):
    res = []
    for i in list:
        if i not in res:
            res.append(i)
    return res

#Returns a list of urls from a website
def urlGrab(url):
    try:
        UrlList = []
        headers = ({'User-Agent': 'Mozilla/5.0'})
        request = Request(url, headers=headers)
        HTMLNEW = urlopen(request).read().decode('latin-1')
        extractor = URLExtract()
        urlList = extractor.find_urls(HTMLNEW)
        return urlList
    except:
        pass

#Deletes all nones from a list
def removeNone(list):
    res = []
    for item in list:
        if item != None :
            res.append(item)
    return res

#Take only domains and sort out duplicates in list
def listSort(list):
    list = removeNone(list)
    length = len(list)
    res = []
    for i in range(length):
        res.append(convert(list[i]))
    res = dupRemove(res)
    res = removeNone(res)
    return res

#Grabs 3 first links from a list thats not already visited
def listGrab(list):
    x = 0
    i = 0
    threeList = []
    while i < 3:
        if list[x] not in visitedUrls:
            threeList.append(list[x])
            x = x+1
            i = i+1
        else:
            x = x+1
    return threeList

#####################################################################

#URL to start crawling
startUrl = 'http://www.lth.se'
visitedUrls.append(startUrl)

#Grabs 3 urls from our starting url
list = urlGrab(startUrl)
list = listSort(list)
visitedUrls = visitedUrls + listGrab(list)

#Grabs 9 urls from 3 previous links
counter = 1
for i in range(3):
    list = urlGrab(visitedUrls[counter])
    try:
        list = listSort(list)
        visitedUrls = visitedUrls + listGrab(list)
    except:
        for i in range (3):
            visitedUrls.append('Dead end/No more new links/Website is blocked')
    counter = counter + 1

#Grabs a total of 27 urls from 9 previous links
for i in range (9):
    list = urlGrab(visitedUrls[counter])
    try:
        list = listSort(list)
        visitedUrls = visitedUrls + listGrab(list)
    except:
        for i in range (3):
            visitedUrls.append('Dead end/No more new links/Website is blocked')
    counter = counter + 1

for i in range(5):
    print()
print('---------------------------------------------------------------------------------------------------------------')
for i in range(5):
    print()

#3x for loops that prints out all links
urlCounter = 1
for i in range(3):
    print(visitedUrls[0],'-->' , visitedUrls[urlCounter])
    urlCounter = urlCounter +1

for i in range (3):
    for j in range(3):
        print('   ',visitedUrls[i+1],'-->' , visitedUrls[urlCounter])
        urlCounter = urlCounter + 1

for i in range (9):
    for j in range(3):
        try:
            print('      ',visitedUrls[i+4],'-->' , visitedUrls[urlCounter])
        except:
            print('      ',visitedUrls[i+4],'-->' , 'End of line')
        urlCounter = urlCounter + 1
