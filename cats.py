from lxml import html
import requests
import urllib

def funnycatpix(path,cats_count,randomize=True):
    i=1
    pages=421
    cats=0
    while i<=pages:
        if randomize == True:
            import random
            i = random.randint(1,421)
            pages=423
            print(i)
        if i==1:
            page = requests.get('http://www.funnycatpix.com/')
        else:
            page = requests.get('http://www.funnycatpix.com/pictures_'+str(i)+'.htm')
        tree = html.fromstring(page.content)
        img = tree.xpath('//img/@src')
        q=0
        while len(img)>q:
            lenq = img[q].find('_t.jpg',1,100)
            name = img[q][:lenq]+'.jpg'
            try: name.index('www', 1, 100)
            except ValueError:
                q+=1
                print('Not Cats detected on this photo')
            else:
                filename = name.replace('http://www.funnycatpix.com/_pics/', '')
                urllib.request.urlretrieve(name, path + filename)
                cats+=1
                print('Cats geted : ',cats)
                q+=1
            if cats_count==cats:
                print('Geted ',cats_count,' cats from funnycatpix success')
                return True
        i+=1
    print('Congratulations! You get all cats from funnycatpix.')


funnycatpix('/',10,False) #img/

