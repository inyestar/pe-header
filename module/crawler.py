import os
import uuid
import requests
from bs4 import BeautifulSoup
import urllib


def get_exe_urls(url):
    # TODO validate url
    text = get_body(url)
    if not text:
        return None
    return parse_text(text)


def get_body(url):
    response = requests.get(url=url)
    # TODO catch error from requests
    if not response:
        return None
    return response.text


def save_exe(url):
    file_name = os.path.join(os.environ['APP_TEMP_DIR'], str(uuid.uuid4())) + '.exe'
    urllib.request.urlretrieve(url, file_name)
    if os.path.exists(file_name):
        return file_name
    return None


def parse_text(text):
    soup = BeautifulSoup(text, "lxml")
    a_list = soup.find_all('a')
    if not a_list or len(a_list) == 0:
        return None
    urls = list()
    for a in a_list:
        if a['href'].endswith('exe') and a['href'].startswith('http'):
            urls.append(a['href'])
    return urls


# TODO delete temp file