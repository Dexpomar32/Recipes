recipes = {
    "Omelette": ["egg", "milk", "salt"],
    "Greek Salad": ["tomato", "cucumber", "feta cheese", "oil", "salt"],
    "Pasta with Sauce": ["pasta", "tomato sauce", "oil", "salt"]
}


def add_recipe():
    name = input("Enter recipe name: ").strip()

    ingredients_input = input("Enter ingredients separated by commas: ")
    ingredients_raw = ingredients_input.lower().split(",")
    
    ingredients = []
    for item in ingredients_raw:
        clean_item = item.strip()
        if clean_item != "":
            ingredients.append(clean_item)

    if name in recipes:
        print("This recipe already exists.")
    else:
        recipes[name] = ingredients
        print("Recipe added successfully.")


def show_possible_recipes():
    available_input = input("Enter your available ingredients (comma separated): ")
    raw_items = available_input.lower().split(",")

    available_ingredients = []
    for item in raw_items:
        clean_item = item.strip()
        if clean_item != "":
            available_ingredients.append(clean_item)

    found_any = False
    for recipe_name in recipes:
        all_present = True
        for ingredient in recipes[recipe_name]:
            if ingredient not in available_ingredients:
                all_present = False

        if all_present:
            print("- " + recipe_name)
            found_any = True

    if not found_any:
        print("No matching recipes found.")


def suggest_alternative_recipes():
    available_input = input("Enter your available ingredients (comma separated): ")
    raw_items = available_input.lower().split(",")

    available_ingredients = []
    for item in raw_items:
        clean_item = item.strip()
        if clean_item != "":
            available_ingredients.append(clean_item)

    found_any = False
    for recipe_name in recipes:
        missing_count = 0
        missing_items = []

        for ingredient in recipes[recipe_name]:
            if ingredient not in available_ingredients:
                missing_count += 1
                missing_items.append(ingredient)

        if missing_count <= 2:
            print("- " + recipe_name + " (missing: " + ", ".join(missing_items) + ")")
            found_any = True

    if not found_any:
        print("No alternative suggestions found.")
