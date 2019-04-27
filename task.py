# 1. Получить количество учеников с сайта geekbrains.ru:
# a) при помощи регулярных выражений,
# b) при помощи библиотеки BeautifulSoup.

import re
from bs4 import BeautifulSoup as BS


# re
with open('index.html') as f:
    code = f.read()

pattern = re.findall ("<span class=\"total-users\">.*?(\d+\s\d+\s\d+)", code)
list2string = ''.join(pattern)
print("Количество учеников на данный момент: ", list2string)

#  bs4
soup = BS (code, "html.parser")
link = soup.find("span", {"class" : "total-users"}).string
link = re.findall('\d+', link)
print("Количество учеников на данный момент: ", link[0],link[1], link[2] )
