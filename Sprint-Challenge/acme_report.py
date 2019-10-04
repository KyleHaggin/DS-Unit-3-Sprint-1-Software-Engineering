from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for x in range(num_products):
        hldr_name = ADJECTIVES[randint(0, 4)] + ' ' + NOUNS[randint(0, 4)]
        plchldr = Product(hldr_name, randint(5, 100), randint(5, 100),
                          uniform(0.0, 2.5))
        products.append(plchldr)
    return products


def inventory_report(products):
    prod_list = generate_products()
    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())
