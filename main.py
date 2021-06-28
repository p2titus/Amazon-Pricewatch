import pricewatch
PROD_FILE_NAME = 'products.json'


def main():
    link, price = get_product_params()
    pricewatch.pricewatch(link, price)
    print('bought products')


def get_product_params():
    # we assume the input file is in json
    import json
    file = open(PROD_FILE_NAME, 'r')
    products = json.loads(file.read())
    file.close()
    return products


if __name__ == '__main__':
    main()
