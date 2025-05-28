import recipes

while True:
    print("\n=== RECIPE GENERATOR ===")
    print("1. Add a new recipe")
    print("2. Show possible recipes")
    print("3. Suggest alternative recipes")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        recipes.add_recipe()

    elif choice == "2":
        recipes.show_possible_recipes()

    elif choice == "3":
        recipes.suggest_alternative_recipes()

    elif choice == "4":
        break
    else:
        print("Invalid option. Please try again.")