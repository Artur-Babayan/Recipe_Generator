from recipe_manager import RecipeManager
import json


def main():
    manager = RecipeManager()

    amount_of_persons = 2
    dish_type = "salad"
    max_cooking_time = 20
    allergie_list = ["nuts", "gluten"]
    diet_requirements = ["vegan"]
    cuisine_list = "Italian"
    output_data_format = """JSON with parameters: "Name", "CookingTime", "RequiredTools", "Ingredients", "Step-by-step directions" and "Ingredients" with parameters: "Name", "grams", "ml", "cups", "teaspoons", "tablespoons", "piece"."""

    full_recipe = manager.generate_full_recipe(amount_of_persons,
                                               dish_type,
                                               max_cooking_time,
                                               allergie_list,
                                               diet_requirements,
                                               cuisine_list,
                                               output_data_format
                                               )

    if full_recipe:
        print(json.dumps(full_recipe, indent=2))


if __name__ == "__main__":
    main()
