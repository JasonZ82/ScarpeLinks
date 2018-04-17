import requests
import re
from bs4 import BeautifulSoup
import sys
from pathlib import Path
#Function to find all links in a webpage.
def find_all_link(url):
    #Request the webpage and encode as utf-8
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text,'lxml')
    #raw_links to save the unorganized links
    #links to save the final links
    raw_links,links = [],[]
    for a in soup.find_all('a'):
        link = a['href']
        if link not in raw_links and link !='': #filter out the same link and empty link
            raw_links.append(link)
    for link in raw_links:
        if link[0] == '/': #Check if the link is inside the web
            full_link = url + link
            if full_link != url+'/' and full_link not in links:#filter out the same link and original link
                links.append(full_link)
        elif link[0] == 'h' and link not in links:
            links.append(link)
    return links
def main():
    if len(sys.argv) == 1:
        print("Usage: {0} URL [URL]...".format(Path(sys.argv[0]).name))
        sys.exit(1)
    # else, if at least one parameter was passed
    for url in sys.argv[1:]:
        try:
            links = find_all_link(url)
        except:
            links = find_all_link('http://'+url)
    #print out the result link
    print(str(len(links)) +' links find\n')
    for link in links:
    	print(link)
if __name__ == "__main__":
    main()