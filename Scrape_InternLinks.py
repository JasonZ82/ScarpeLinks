import requests
import re
from bs4 import BeautifulSoup
import sys
from pathlib import Path

raw_links,links, internlink = [],[],[]
def find_all_link(oriurl, url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text,'lxml')
    for a in soup.find_all('a'):
        try:
            link = a['href']
            if link not in raw_links and link !='':
                raw_links.append(link)
        except:
            pass

    for link in raw_links:
        if link[0] == '/' and link not in links and link not in internlink:
            internlink.append(link)
            full_link = oriurl + link
            if full_link != oriurl+'/' and full_link not in links:
                print('Work on:'+full_link)
                links.append(full_link)
                find_all_link(oriurl,full_link)
        elif link[0] == 'h' and link not in links:
            if oriurl in link:
                links.append(link)
                print('Work on:'+link)
                find_all_link(oriurl,link)
def main():
    if len(sys.argv) == 1:
        print("Usage: {0} URL [URL]...".format(Path(sys.argv[0]).name))
        sys.exit(1)
    # else, if at least one parameter was passed
    
    for url in sys.argv[1:]:
        try:
            oriurl = url
            find_all_link(oriurl, url)
            
        except:
            oriurl= 'http://'+url
            find_all_link(oriurl, 'http://'+url)

if __name__ == "__main__":
    main()