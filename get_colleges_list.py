import requests
import lxml
from bs4 import BeautifulSoup


def get_100_colleges(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    colleges = []
    h2 = soup.find_all('h2', 'ct-slideshow__slide__text-container__caption')
    for i in h2:
        i = i.text
        if '.' in i:
            cc_name = i.split('. ')[-1].replace('\n', '')
            colleges.append(cc_name)
    return colleges


def get_colleges_website(colleges_list: list):
    print(colleges_list)


if __name__ == '__main__':
    colleges_list_url = "https://stacker.com/stories/1803/100-best-community-colleges-america"
    colleges_list = get_100_colleges(colleges_list_url)
    get_colleges_website(colleges_list)
