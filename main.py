import json
from ingredients import comedogenic_ingredients


def get_risk_level(score):
    if score == 0:
        return "Low"
    elif score <= 2:
        return "Medium"
    else:
        return "High"


def check_product(product):
    flagged = []

    for ingredient in product["ingredients"]:
        if ingredient.lower() in comedogenic_ingredients:
            flagged.append(ingredient)

    score = len(flagged)
    return flagged, score


def main():
    with open("products.json") as f:
        products = json.load(f)

    for product in products:
        flagged, score = check_product(product)
        risk_level = get_risk_level(score)

        print(f"\nProduct: {product['name']}")
        print("Flagged Ingredients:", flagged if flagged else "None")
        print("Acne Risk Score:", score)
        print(f"Risk Level: {risk_level}")
        print("-" * 40)


if __name__ == "__main__":
    main()
