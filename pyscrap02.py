# coding: utf-8

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs

def gettag(url, tag):
    try:
        html_page = urlopen(url)

    except HTTPError as e:
        return "HTTPError"

    if not(html_page is None):
        html_string = html_page.read()
        bs_obj = bs(html_string, "lxml")

        bad_content_str = "bs_obj." + tag

        try:
            bad_content = eval(bad_content_str)

        except AttributeError as e:
            return "Non existent tag."

        else:
            if bad_content == None:
                return "Tag was not found."
            else:
                return bad_content
    else:
        return "This site is empty."

def execute():
    print(gettag("http://pythonscraping.com/pages/page1.html", "h1"))

if __name__ == "__main__":
    execute()
