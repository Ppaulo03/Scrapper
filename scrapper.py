import requests
import pprint
from bs4 import BeautifulSoup


def clean_hn(links, subtext):

    hn = []
    for idx, item in enumerate(links):
        vote = subtext[idx].select('.score')
        if len(vote):
            value = int(vote[0].getText().replace(' points', ''))
            if value > 99:
                title = links[idx].getText()
                href = links[idx].get('href', None)
                hn.append({'title': title, 'link': href, 'votes': value})
    return hn


def hn_new_page(num):
    hn = []
    for i in range(1, num+1):
        link = 'https://news.ycombinator.com/news?p=' + str(i)
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        hn = hn + clean_hn(links, subtext)

    hn.sort(key=lambda dic: dic['votes'], reverse=True)
    return hn


pprint.pprint(hn_new_page(2))
