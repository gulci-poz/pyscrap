# coding: utf-8

from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs

try:
    # w przypadku braku serwera urlopen() zwraca None
    html_page = urlopen("http://pythonscraping.com/pages/page1.html")

except HTTPError as e:
    print(e)

else:
    # niepotrzebne jeśli w except damy return lub break
    print("Data retrieved")

# read() działa jak pop, przy następnym użyciu nie dostaniemy zawartości strony, więc zapamiętamy ją w osobnej zmiennej
# dostaniemy tekst w postaci: b'zawartość_strony'
# pusta strona: b''

# dodajemy drugi parametr "lxml", jest to parser; lxml jest domyślny, ale nie musi być tak na każdym systemie, warto explicite wybrać parser
# brak szukanego tagu: None
# błędny tag: AttributeError
# wyszukuje wszystkie h1 w strukturze, można też podać inny wariant ścieżki: html.body.h1, body.h1, html.h1

if not(html_page is None):
    html_string = html_page.read()
    bs_obj = bs(html_string, "lxml")

    try:
        # badContent ma zasięg poza try
        bad_content = bs_obj.h1

    except AttributeError as e:
        print("Non existent tag.")

    else:
        if bad_content == None:
            print("Tag was not found.")
        else:
            print(bad_content)
else:
    print("This site is empty.")

# eval używamy dla wyrażenia, np. bs_obj.h1
# exec używamy dla instrukcji, np. print("hello")
