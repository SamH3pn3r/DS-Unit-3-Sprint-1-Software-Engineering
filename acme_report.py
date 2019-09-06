from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for _ in range(num_products):
        product = Product(name=str(sample(ADJECTIVES, 1)) +
                          '' + str(sample(NOUNS, 1)),
                          price=randint(5, 100), weight=randint(5, 100),
                          flammability=uniform(0, 2.5))
        products.append(product)
    return products


def inventory_report(products):
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    names = []
    for x in range(len(products)):
        names.append(products[x].name)
    name_set = set(names)
    unique_names = len(name_set)
    print("Number of unique names: ", unique_names)

    prices = []
    for x in range(len(products)):
        prices.append(products[x].price)
    avg_price = sum(prices)/len(prices)
    print(f'Average price: ${avg_price:.2f}')

    weights = []
    for x in range(len(products)):
        weights.append(products[x].weight)
    avg_weight = sum(weights)/len(weights)
    print("Average weight:", avg_weight)

    flames = []
    for x in range(len(products)):
        flames.append(products[x].flammability)
    avg_flame = sum(flames)/len(flames)
    print("Average flammability:", avg_flame)


if __name__ == '__main__':
    inventory_report(generate_products())
