from selectorlib import Extractor
import requests
from time import sleep
DELAY = 24 * 60 * 60  # wait 15 minutes
from threading import Thread, Barrier

HEADERS = {
    'authority': 'www.amazon.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/51.0.2704.64 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-4mode': 'navigate',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}


def pricewatch(products):
    '''print(len(products))
    print(products)'''
    no_products = len(products)
    if no_products >= 1:
        threads = []
        b = Barrier(no_products)
        for product in products:
            x = products[product]
            threads.append(Thread(target=__agent(x['link'], x['price'], b)))
        for t in threads:
            t.start()
    else:
        print("no products specified - terminating")


def __agent(link, price, b: Barrier):
    purchased = False
    while not purchased:
        r = requests.get(link, headers=HEADERS)
        if r.status_code < 500:
            purchased = __watch_price(price, r)
            if purchased is True:
                __purchase(link)
        if not purchased:
            sleep(DELAY)
    b.wait()


def __watch_price(price, r):
    product_data = r.text
    e = Extractor.from_yaml_file('amazon-layout.yml')
    xs = e.extract(product_data)
    print(xs)
    x = xs['price']
    return x is not None and float(x[1:]) <= price


def __purchase(link):
    print("success for now!")
    # TODO - implement
    return None
