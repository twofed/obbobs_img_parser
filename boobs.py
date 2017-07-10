from lxml import html
import requests
import urllib

i=0
raz=1 # * 20 img
path='/' # img/

class get_boobs():
    while raz!=i:
        i += 1
        page = requests.get('http://oboobs.ru/'+str(i)+'/')
        tree = html.fromstring(page.content)
        img = tree.xpath('//img/@src')
        q=0
        while len(img)>q:
            lenq = img[q].find('w/',1,50)
            name = img[q][lenq+2:]
            try: img[q].index('_preview', 1, 40)
            except ValueError:
                q+=1
            else:
                img[q] = img[q].replace('_preview', '')
                urllib.request.urlretrieve(img[q], path + name)
                q+=1


