import time

import requests
import lxml
import os
import googlesearch
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
            colleges.append(cc_name + ' computer science')
            with open('colleges_list.txt', 'a', encoding='utf-8') as f:
                f.write(cc_name + ' computer science' + '\n')
    print(len(colleges))
    return colleges


def get_colleges_website():
    with open('colleges_list.txt', 'r', encoding='utf-8') as f:
        colleges_list = f.readlines()
    index = 0
    for i in colleges_list:
        index += 1
        result = list(googlesearch.search(i, num_results=1))[0]
        with open('used_list.txt', 'a', encoding='utf-8') as f:
            f.write(i)
        with open('websites_list.txt', 'a', encoding='utf-8') as f:
            f.write(i)
            f.write(result + '\n\n')
        print("Index: {} \nCollege: {}Result: {}\n".format(index, i, result))


if __name__ == '__main__':
    colleges_list_url = "https://stacker.com/stories/1803/100-best-community-colleges-america"
    # colleges_list = get_100_colleges(colleges_list_url)
    get_colleges_website()
