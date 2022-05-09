import time
import requests
import lxml
import os
import re
import googlesearch
import pandas as pd
from bs4 import BeautifulSoup
from tenacity import *


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


# @retry(stop=stop_after_attempt(10), wait=wait_random(min=1, max=2))
def get_email(original_url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.66'
    }
    html = requests.get(original_url, headers=headers).text
    email_list = re.findall("\w+@\w+\.\w+", html)
    print(email_list)
    return email_list


def get_colleges_email():
    with open('websites_list.txt', 'r', encoding='utf-8') as f:
        colleges_list = f.readlines()
        for i in colleges_list:
            if 'https://' in i:
                index = colleges_list.index(i)
                name = colleges_list[index - 1]
                email = get_email(i)
                with open('email_list.txt', 'a', encoding='utf-8') as f:
                    f.write(name)
                    f.write(str(email) + '\n\n')


def get_csv():
    with open('email_list.txt', 'r', encoding='utf-8') as f:
        colleges_list = f.readlines()
        names = []
        emails = []
        for i in colleges_list:
            if '[' in i:
                if i != '[]\n':
                    index = colleges_list.index(i)
                    names.append(colleges_list[index - 1])
                    emails.append(i)
        result = {'College Name': names, 'Email': emails}
        print(result)
        df = pd.DataFrame(result)
        # 保存 dataframe
        df.to_csv('result.csv')


if __name__ == '__main__':
    colleges_list_url = "https://stacker.com/stories/1803/100-best-community-colleges-america"
    # colleges_list = get_100_colleges(colleges_list_url)
    # get_colleges_website()
    # get_colleges_email()
    get_csv()
