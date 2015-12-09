from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
import requests


FUZZ_MIN = 75


def search_apmex(query):
    def parse_search_items(content, query):
        soup = BeautifulSoup(content, 'lxml')
        products = soup.find_all('div', attrs={'class': 'product-item product-item-horizontal'})
        possible = []
        for product in products:
            title_tag = product.select('div.product-item-title')[0]
            title = title_tag.text.strip()
            if fuzz.partial_ratio(title.lower(), query.lower()) >= FUZZ_MIN:
                link = title_tag.a.attrs['href']  # relative
                img_link = product.select('div.product-item-image')[0].img.attrs['src']
                try:
                    table = product.select('table.table-volume-pricing')[0]
                except:
                    table = ''
                if table:
                    price = table.tbody.find_all('td')[1].text  # gets the low tier cash price
                    # headers = [header.text for header in table.select('thead tr th')]
                    # prices = [{headers[i]: cell.text for i, cell in enumerate(row.select("td"))} for row in table.select("tbody tr")]
                else:
                    price = ''  # []
                possible.append({'title':title, 'url':link, 'img':img_link, 'price':price})
        return possible

    base = 'http://www.apmex.com{}'
    search = '/search?q={}'
    url = base.format(search.format(query))
    req = requests.get(url)
    results = parse_search_items(req.content, query)
    for res in results:
        res['url'] = base.format(res['url'])
    return results


def search_provident(query):
    def parse_search_items(content, query):
        soup = BeautifulSoup(content, 'lxml')
        items = soup.select('div.item')
        possible = []
        for item in items:
            title = item.h5.a.attrs['title'].strip()
            if fuzz.partial_ratio(title.lower(), query.lower()) >= FUZZ_MIN:  
                link = item.h5.a.attrs['href']
                img_link = item.select('div.image-wrapper')[0].img.attrs['src']
                sku = item.find_parent('div', attrs={'class':'item-wrapper'}).attrs['rel']
                if sku:
                    req = requests.get('http://www.providentmetals.com/services/products.php?type=product&sku='+sku)
                    data = req.json()
                    if data[0]['inStock']:
                        price = data[0]['price']
                    else:
                        price = ''
                else:
                    price = ''
                possible.append({'title':title, 'url':link, 'img':img_link, 'price':price})
        return possible

    base = 'http://www.providentmetals.com{}'
    search = '/catalogsearch/result/?q={}'
    url = base.format(search.format(query))
    req = requests.get(url)
    results = parse_search_items(req.content, query)
    return results


def search_jmbullion(query):
    def parse_search_items(content, query):
        soup = BeautifulSoup(content, 'lxml')
        items = soup.select('div.product')
        possible = []
        for item in items:
            pass  # getting page doesnt actually get the page right now
        return possible

    base = 'http://www.jmbullion.com'
    search = '/search/?q={}'
    url = base.format(search.format(query))
    req = requests.get(url)
    results = parse_search_items(req.content, query)
    return results


def search_shinybars(query):
    def parse_search_items(content, query):
        soup = BeautifulSoup(content, 'lxml')
        items = soup.select('div.product-item')
        possible = []
        for item in items:
            title = item.h2.text.strip()
            if fuzz.partial_ratio(title.lower(), query.lower()) >= FUZZ_MIN:
                link = item.a.attrs['href']
                img_link = item.img.attrs['src']
                price = item.select('div.prices')[0].text.replace('$', '')
                possible.append({'title':title, 'url':link, 'img':img_link, 'price':price})
        return possible

    base = 'https://www.shinybars.com{}'
    search = '/filterSearch?q={}'
    url = base.format(search.format(query))
    req = requests.get(url)
    results = parse_search_items(req.content, query)
    for result in results:
        result['url'] = base.format(result['url'])
    return results


def search_goldeneaglecoins(query):
    def parse_search_items(content, query):
        soup = BeautifulSoup(content, 'lxml')
        possible = []
        items = soup.select('li.product-information')
        for item in items:
            title = item.h2.a.text.strip()
            if fuzz.partial_ratio(title.lower(), query.lower()) >= FUZZ_MIN:
                link = item.h2.a.attrs['href']
                img_link = item.img.attrs['src']
                price = item.fieldset.strong.text.strip().replace('$', '').replace(',', '')
                possible.append({'title':title, 'url':link, 'img':img_link, 'price':price})
        return possible

    base = 'https://www.goldeneaglecoin.com{}'
    search = '/search?searchText={}'
    url = base.format(search.format(query))
    req = requests.get(url)
    results = parse_search_items(req.content, query)
    for result in results:
        result['url'] = base.format(result['url'])
    return results


def search_silvertowne(query):
    def parse_search_items(content, query):
        soup = BeautifulSoup(content, 'lxml')
        possible = []
        items = soup.select('div.productResult')
        for item in items:
            title = item.a.attrs['title'].strip()
            if fuzz.partial_ratio(title.lower(), query.lower()) >= FUZZ_MIN:
                link = item.a.attrs['href']  # relative
                img_link = item.img.attrs['src']  # relative
                price = item.select('p.featuredPrice')[0].text.strip()
                possible.append({'title':title, 'url':link, 'img':img_link, 'price':price})
        return possible

    base = 'http://www.silvertowne.com{}'
    search = '/vsearch.aspx?SearchTerm={}'
    url = base.format(search.format(query))
    req = requests.get(url)
    results = parse_search_items(req.content, query)
    for result in results:
        result['url'] = base.format(result['url'])
        result['img'] = base.format(result['img'])
    return results


def search_gainesvillecoins(query):
    def parse_search_items(content, query):
        soup = BeautifulSoup(content, 'lxml')
        possible = []
        items = soup.select('div.gridItem')
        for item in items:
            title = item.select('div.title')[0].a.attrs['title']
            if fuzz.partial_ratio(title.lower(), query.lower()) >= FUZZ_MIN:
                link = item.select('div.title')[0].a.attrs['href']  # relative
                img_link = 'http:' + item.img.attrs['data-original']
                price = item.select('div.price')[0].text
                possible.append({'title':title, 'url':link, 'img':img_link, 'price':price})
        return possible

    base = 'http://www.gainesvillecoins.com{}'
    search = '/search?&s={}'
    url = base.format(search.format(query))
    req = requests.get(url)
    results = parse_search_items(req.content, query)
    for result in results:
        result['url'] = base.format(result['url'])
    return results

