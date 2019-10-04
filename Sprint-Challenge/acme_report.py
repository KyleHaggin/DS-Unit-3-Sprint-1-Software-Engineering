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
    price_sum = 0
    weight_sum = 0
    flame_sum = 0
    prod_names = []
    length = len(prod_list)
    for x in range(0, length):
        price_sum = price_sum + prod_list[x].price
        weight_sum = weight_sum + prod_list[x].weight
        flame_sum = flame_sum + prod_list[x].flammability
        prod_names.append(prod_list[x].name)
    print('Unique product names: ' + str(len(set(prod_names))))
    print('Average price: ' + str(price_sum / length))
    print('Average weight: ' + str(weight_sum / length))
    print('Average flammability ' + str(flame_sum / length))
    pass


if __name__ == '__main__':
    inventory_report(generate_products())
