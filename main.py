import json
from ingredients import comedogenic_ingredients


def check_product(product):
    flagged = []

    for ingredient in product["ingredients"]:
        if ingredient.lower() in comedogenic_ingredients:
            flagged.append(ingredient)

    return flagged, len(flagged)


def main():
    with open("products.json") as f:
        products = json.load(f)

    for product in products:
        flagged, score = check_product(product)

        print(f"\nProduct: {product['name']}")
        print("Flagged Ingredients:", flagged if flagged else "None")
        print("Acne Risk Score:", score)
        print("-" * 40)


# THIS LINE IS CRITICAL
if __name__ == "__main__":
    main()