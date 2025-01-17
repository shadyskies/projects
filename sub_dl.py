import requests 
from bs4 import BeautifulSoup
import os
import urllib
import zipfile, io

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})


# using opensubs api to get subs 
# def getid(query):
#     load_dotenv()
#     url = "https://api.opensubtitles.com/api/v1/subtitles/"
#     query_string = {"query": query}
#     headers = {"Api-Key": os.getenv('opensub_api_key')}

#     response = requests.request("GET", url, headers=headers, params=query_string)
#     val = json.loads(response.text)

#     with open('json_file.json', 'w') as file:
#         json.dump(val, file, indent=4, sort_keys=True)

# getid('Avengers Endgame')
DOWNLOAD_URL = "https://yts-subs.com/"


#TODO: download zip from url
def download_url(url):
    response = requests.get(url)
    with open('faj.zip', 'wb') as outfile:
        outfile.write(response.content)


#TODO: check if movie exists or not
def get_movie(query):
    url = DOWNLOAD_URL + 'search/' + query
    response = requests.get(url, HEADERS)
    print(response.status_code)
    soup = BeautifulSoup(response.content, features='html.parser')
    div_tags = soup.find_all('div',{'class':'media-body'})
    links = [i.findChildren('a', recursive=False)[0]['href'] for i in div_tags]
    names = soup.find_all('h3', {'class': 'media-heading'})
    names = [i.get_text() for i in names]
    # print(names)
    return links, names

def choose_movie(links, names):
    print('Select movie:')
    for i in range(len(names)):
        print(f"{i}. {names[i]}")
    sel = int(input())
    return DOWNLOAD_URL + links[sel]

def sel_sub(url):
    response = requests.get(url, HEADERS)
    # print(response.status_code)
    soup = BeautifulSoup(response.content, features='html.parser')
    dl_links = soup.find_all('a',{'class':'subtitle-download'})
    dl_links = [i['href'] for i in dl_links]
    print('Select sub:')
    for i in range(len(dl_links)):
        print(f"{i}. {dl_links[i]}")
    sel = int(input())
    return DOWNLOAD_URL + dl_links[sel]


def main_dl(url):
    response = requests.get(url, HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    link = soup.find_all('a',{'class': 'btn-icon download-subtitle'})
    link = link[0]['href']
    print(f"Ctrl + Click here:{link}")
    # download_url(url=url)


links, names = get_movie(input("Enter movie to download of:"))
url = choose_movie(links, names)
url = sel_sub(url)
main_dl(url)